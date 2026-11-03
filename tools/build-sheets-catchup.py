"""Build the Sheets Foundation catch-up start files.

    python tools/build-sheets-catchup.py

Writes shared/sample-files/catch-up/GW-Sheets-start-LabNN.xlsx for Labs 02 to 08.
Each file is the course workbook as it should look at the start of that lab: the
supplied TaskRegister.xlsx with every earlier lab's guided steps applied. Pasted
text comes from the copy blocks in the lab READMEs, so the files stay in step
with the lessons. Independent practice is not included.

A participant who missed a lab uploads the file, chooses File > Save as Google
Sheets and renames the copy GW - Sheets - Task Register. Filter views are a
Google Sheets feature and can't be stored in an Excel file, so the Lab 08 start
file has none; the lab tells participants to recreate the two views.
"""
import copy
import datetime
import re
from pathlib import Path

import openpyxl
from openpyxl.chart import BarChart, Reference
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.workbook.defined_name import DefinedName
from openpyxl.worksheet.datavalidation import DataValidation

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "04-sheets-foundation-intermediate"
OUT = ROOT / "shared/sample-files/catch-up"

RM = '"RM"#,##0'
RM2 = '"RM"#,##0.00'
DATE = "dd/mm/yyyy"
PRACTICE_DATE = datetime.datetime(2026, 10, 24)
LIGHT_BLUE = PatternFill("solid", fgColor="CFE2F3")
WRAP = Alignment(wrap_text=True, vertical="top")


# ---- reading copy blocks from the lessons -------------------------------------

def blocks(lab, section):
    """The ```text blocks in one ## section of a lab README, as lists of rows."""
    text = next(COURSE.glob(f"{lab:02d}-*/README.md")).read_text(encoding="utf-8")
    m = re.search(r"^## " + re.escape(section) + r".*?(?=^## |\Z)", text, re.S | re.M)
    if not m:
        raise SystemExit(f"Lab {lab}: no section {section}")
    out = []
    for b in re.findall(r"```text\n(.*?)```", m.group(0), re.S):
        out.append([line.split("\t") for line in b.rstrip("\n").split("\n")])
    return out


def put(ws, top_left, rows, fmt=None):
    """Write rows of text from a cell. Numbers and formulas keep their type."""
    c0 = ws[top_left]
    for r, row in enumerate(rows):
        for c, val in enumerate(row):
            if val == "":
                continue
            cell = ws.cell(row=c0.row + r, column=c0.column + c)
            cell.value = number(val)
            if fmt and isinstance(cell.value, (int, float)):
                cell.number_format = fmt


def number(val):
    if re.fullmatch(r"-?\d+", val):
        return int(val)
    if re.fullmatch(r"-?\d+\.\d+", val):
        return float(val)
    return val


def widths(ws, **w):
    for col, width in w.items():
        ws.column_dimensions[col].width = width


def wrap(ws, rng):
    for row in ws[rng]:
        for cell in row:
            cell.alignment = WRAP


def fmt(ws, rng, number_format):
    for row in ws[rng]:
        for cell in row:
            cell.number_format = number_format


def duplicate(wb, ws, title):
    new = wb.copy_worksheet(ws)
    new.title = title
    new.freeze_panes = ws.freeze_panes
    return new


def order(wb, names):
    assert sorted(names) == sorted(wb.sheetnames), (names, wb.sheetnames)
    wb._sheets = [wb[n] for n in names]
    wb.active = 0


# ---- what each lab adds ------------------------------------------------------

def lab01(wb):
    tasks = wb["Tasks"]
    nav = duplicate(wb, tasks, "Navigation Practice")
    nav["J1"] = "Practice only"
    widths(nav, J=18)

    guide = wb.create_sheet("Workbook Guide")
    put(guide, "A1", blocks(1, "1.5")[0])
    put(guide, "A7", blocks(1, "1.6")[0])
    put(guide, "C8", [["T001", "T001"], ["Aina Rahman", "T004"], ["Complete", "T007"], ["0", "T012"]])
    put(guide, "A13", blocks(1, "1.8")[0])
    put(guide, "A23", blocks(1, "1.9")[0])
    widths(guide, A=22, B=90, C=16, D=12)

    entry = wb.create_sheet("Entry Practice")
    put(entry, "A1", blocks(1, "1.7")[0])
    put(entry, "A2", [
        ["T001", "Planning", "Confirm reporting fields", "Aina Rahman", "1", "Complete", "600", "550"],
        ["T002", "Planning", "Draft status definitions", "Bala Kumar", "1", "In Progress", "800", "700"],
        ["T003", "Planning", "Review pilot brief", "Siti Aminah", "1", "Not Started", "500", "0"],
    ])
    widths(entry, C=28)
    order(wb, ["Tasks", "Workbook Guide", "Navigation Practice", "Entry Practice", "Summary"])


def lab02(wb):
    tasks, nav, entry = wb["Tasks"], wb["Navigation Practice"], wb["Entry Practice"]
    fmt(tasks, "G2:H13", RM)
    fmt(tasks, "E2:E13", "0")
    wrap(tasks, "C2:C13")

    nav["J2"] = PRACTICE_DATE
    nav["J2"].number_format = DATE
    nav["J4"], nav["K4"] = "Numeric cost", "Text cost"
    nav["J5"], nav["K5"] = 600, "RM 600"
    nav["J5"].number_format = RM

    put(entry, "A7", blocks(2, "2.5")[0])
    entry["B12"] = PRACTICE_DATE
    entry["B12"].number_format = DATE
    fmt(entry, "B9:B10", RM)
    entry["A14"], entry["B14"] = "Temporary SUM check", "=SUM(B9:B10)"
    entry["A15"], entry["B15"] = "Numeric input count", "=COUNT(B9:B10)"
    entry["B14"].number_format = RM
    fmt(entry, "G2:H4", RM)
    fmt(entry, "E2:E4", "0")
    for cell in entry["A1:H1"][0]:
        cell.font = Font(bold=True)
        cell.fill = LIGHT_BLUE
    wrap(entry, "C2:C4")

    put(entry, "D7", blocks(2, "2.7")[0])
    entry["D9"], entry["E9"], entry["F9"] = 600, 600, 123
    fmt(entry, "D9:F9", RM)

    put(entry, "A17", blocks(2, "2.8")[0])
    entry["B22"], entry["B23"] = "=COUNT(Tasks!G2:H13)", "=COUNT(Tasks!E2:E13)"
    wrap(entry, "B17:B24")
    widths(entry, A=22, B=60)


def lab03(wb):
    tasks, nav = wb["Tasks"], wb["Navigation Practice"]
    tasks["I1"] = "Variance"
    for r in range(2, 14):
        tasks[f"I{r}"] = f"=H{r}-G{r}"
        tasks[f"I{r}"].number_format = RM
    put(tasks, "K1", blocks(3, "3.2")[0])
    for cell, formula in [("L2", "=SUM(G2:G13)"), ("L3", "=SUM(H2:H13)"), ("L4", "=SUM(I2:I13)"),
                          ("L6", "=AVERAGE(G2:G13)"), ("L7", "=COUNT(G2:G13)")]:
        tasks[cell] = formula
    fmt(tasks, "L2:L4", RM)
    tasks["L6"].number_format = RM2
    widths(tasks, K=20, L=14)

    for cell in ("J2", "J4", "K4", "J5", "K5"):
        nav[cell] = None
    for r in range(2, 14):
        nav[f"J{r}"] = f"=G{r}*$L$9"
        nav[f"J{r}"].number_format = "0.00"
    nav["K9"], nav["L9"] = "Practice multiplier", 1.1
    widths(nav, K=20)

    calc = wb.create_sheet("Calculation Tests")
    b4, b5 = blocks(3, "3.4"), blocks(3, "3.5")
    put(calc, "A1", b4[0])
    for r in range(2, 5):
        calc[f"C{r}"] = f"=B{r}-A{r}"
    put(calc, "D1", b4[1])
    put(calc, "A8", b4[2])
    for r in range(9, 12):
        calc[f"C{r}"], calc[f"D{r}"] = f"=COUNT(B{r})", f"=SUM(B{r})"
    put(calc, "A14", b5[0])
    put(calc, "B15", [["20", "20"], ["-20", "-20"]])
    b6 = blocks(3, "3.6")
    put(calc, "F1", b6[0])
    for r in range(2, 6):
        calc[f"G{r}"], calc[f"H{r}"] = f"=F{r}*K{r}", f"=F{r}*$K$2"
    calc["K1"], calc["K2"] = "Practice multiplier", 1.1
    put(calc, "A19", b6[1])
    put(calc, "B20", [["1.1", "1.2", "1.1"]])
    put(calc, "A23", blocks(3, "3.7")[0])
    calc["B24"] = "=SUM(Tasks!I2:I13)"
    calc["B25"] = "=SUM(Tasks!H2:H13)-SUM(Tasks!G2:G13)"
    calc["B26"] = "=B24-B25"
    fmt(calc, "B24:B26", RM)
    put(calc, "A28", [
        ["Blank Actual", "Not supplied; don't treat it as a confirmed zero."],
        ["Relative G3", "Moved to the empty K3, so it shows 0; that's reference drift."],
        ["Absolute H5", "Keeps $K$2, so it shows 110 after restoring 1.1."],
    ])
    widths(calc, A=22, D=30, K=20)
    order(wb, ["Tasks", "Workbook Guide", "Navigation Practice", "Calculation Tests", "Entry Practice", "Summary"])


def lab04(wb):
    tasks = wb["Tasks"]
    dirty = wb.create_sheet("Dirty Text Practice")
    put(dirty, "A1", [["TaskID", "Team", "Status"], ["T001", " Planning ", "complete"],
                      ["T002", "Procurement", "In Progress"], ["T003", "Site Coordination ", "Not Started"]])
    dirty["D1"] = "CleanTeam"
    put(dirty, "E1", blocks(4, "4.2")[0])
    for r in range(2, 5):
        dirty[f"D{r}"], dirty[f"F{r}"], dirty[f"G{r}"] = f"=TRIM(B{r})", f"=LEN(B{r})", f"=LEN(D{r})"
    widths(dirty, B=20, D=20)

    sorting = duplicate(wb, tasks, "Sorting Practice")
    sorting.freeze_panes = "A2"
    put(sorting, "K9", blocks(4, "4.4")[0])
    sorting["L9"], sorting["L10"], sorting["L11"] = "=SUM(PlannedCosts)", "=SUM(G2:G13)", "=L9-L10"
    fmt(sorting, "L9:L11", RM)
    wb.defined_names["PlannedCosts"] = DefinedName("PlannedCosts", attr_text="'Sorting Practice'!$G$2:$G$13")

    raw = wb.create_sheet("Cleaning Intake Raw")
    put(raw, "A1", blocks(4, "4.5")[0])
    raw["B2"] = "  Planning  "

    intake = wb.create_sheet("Cleaning Intake")
    sorted_rows = [
        ["C001", "  Planning  ", "complete", "Complete", "Case standardised; raw retained"],
        ["C004", "Planning", "Not Started", "Not Started", "Retain"],
        ["C002", "Procurement", "In Progress", "In Progress", "Identical duplicate; retain both"],
        ["C002", "Procurement", "In Progress", "In Progress", "Identical duplicate; retain both"],
        ["C003", "Site Coordination", "Blocked", "Blocked", "Clarify: not a canonical status"],
    ]
    put(intake, "A1", [["TaskID", "Team", "Status", "CleanTeam", "CleanStatus", "Disposition"]])
    for i, (tid, team, status, clean, disp) in enumerate(sorted_rows, start=2):
        intake[f"A{i}"], intake[f"B{i}"], intake[f"C{i}"] = tid, team, status
        intake[f"D{i}"], intake[f"E{i}"], intake[f"F{i}"] = f"=TRIM(B{i})", clean, disp
    put(intake, "A9", blocks(4, "4.6")[0])
    put(intake, "A14", blocks(4, "4.7")[0])
    put(intake, "B15", [["complete", "Complete"], ["In Progress", "In Progress"], ["Blocked", "Blocked"]])
    put(intake, "A19", blocks(4, "4.7")[1])
    intake["B19"], intake["B20"], intake["B21"] = "=SUM(PlannedCosts)", "=SUM('Sorting Practice'!G2:G13)", "=B19-B20"
    fmt(intake, "B19:B21", RM)
    widths(intake, A=14, B=20, C=14, D=20, E=14, F=34)

    safety = duplicate(wb, intake, "Sort Safety Test")
    put(safety, "A24", blocks(4, "4.8")[0])
    put(safety, "C25", [["Blocked", "Complete"], ["In Progress", "In Progress"], ["Not Started", "Blocked"]])
    safety["A29"], safety["B29"] = "Final state", "Disposable test restored; raw intake and original Tasks retained."
    order(wb, ["Tasks", "Sorting Practice", "Cleaning Intake Raw", "Cleaning Intake", "Sort Safety Test",
               "Workbook Guide", "Navigation Practice", "Calculation Tests", "Dirty Text Practice",
               "Entry Practice", "Summary"])


def status_rule(sqref):
    dv = DataValidation(type="list", formula1='"Complete,In Progress,Not Started"', allow_blank=True,
                        showErrorMessage=True, errorStyle="stop")
    for rng in sqref.split():
        dv.add(rng)
    return dv


def lab05(wb):
    tasks = wb["Tasks"]
    tasks.add_data_validation(status_rule("F2:F13 N2"))
    tasks["I15"], tasks["J15"] = "SUM costs", "=SUM(G2:G13)"
    tasks["J15"].number_format = RM

    rules = wb.create_sheet("Rule Tests")
    b4, b5 = blocks(5, "5.4")[0], blocks(5, "5.5")[0]
    put(rules, "A1", b4)
    put(rules, "B2", [["Complete"], ["In Progress"], ["Not Started"]])
    put(rules, "D2", [["Accepted"], ["Accepted"], ["Accepted"], ["Rejected"], ["Clearing allowed"]])
    rules.add_data_validation(status_rule("B2:B6"))
    put(rules, "A9", b5)
    put(rules, "D10", [["Rejected"], ["Accepted"], ["Accepted"], ["Rejected"], ["Rejected"], ["Clearing allowed"]])
    put(rules, "A18", blocks(5, "5.7")[0])
    put(rules, "A27", blocks(5, "5.9")[0])
    put(rules, "C28", [
        ["8", "10400", "T002 T003 T005 T006 T008 T009 T011 T012"],
        ["2", "10400", "T002 T003"],
        ["12", "10400", "All source statuses and formulas retained."],
    ])
    widths(rules, A=24, B=60, C=12, D=16, E=40)

    rule_entry = duplicate(wb, wb["Entry Practice"], "Entry Rule Practice")
    week = DataValidation(type="custom", formula1="AND(ISNUMBER(E2),E2=INT(E2),E2>=1,E2<=4)",
                          showErrorMessage=True, errorStyle="stop", showInputMessage=True,
                          prompt=blocks(5, "5.5")[2][0][0])
    week.add("E2:E4")
    rule_entry.add_data_validation(week)
    order(wb, ["Tasks", "Rule Tests", "Sorting Practice", "Cleaning Intake Raw", "Cleaning Intake",
               "Sort Safety Test", "Workbook Guide", "Navigation Practice", "Calculation Tests",
               "Dirty Text Practice", "Entry Practice", "Entry Rule Practice", "Summary"])


def summary_charts(ws):
    for title, cols, anchor, ytitle in [("Task count by status", (1, 2), "A10", "TaskCount"),
                                        ("Planned cost by team (RM)", (4, 5), "F10", "Planned cost (RM)")]:
        ch = BarChart()
        ch.type = "col"
        ch.title = title
        ch.y_axis.title = ytitle
        ch.legend = None
        ch.add_data(Reference(ws, min_col=cols[1], min_row=1, max_row=4), titles_from_data=True)
        ch.set_categories(Reference(ws, min_col=cols[0], min_row=2, max_row=4))
        ch.width, ch.height = 12, 8
        ws.add_chart(ch, anchor)


def lab06(wb):
    s = wb["Summary"]
    s["G1"], s["D1"] = s["D1"].value, None
    for r in range(2, 5):
        s[f"B{r}"] = f"=COUNTIF(Tasks!$F$2:$F$13,A{r})"
    s["A5"], s["B5"] = "Total", "=SUM(B2:B4)"
    put(s, "D1", blocks(6, "6.2")[0])
    for r in range(2, 5):
        s[f"E{r}"] = f"=SUMIF(Tasks!$B$2:$B$13,D{r},Tasks!$G$2:$G$13)"
    put(s, "G2", blocks(6, "6.6")[0])
    for cell, formula in [("H3", "=B5"), ("I3", "=COUNTA(Tasks!A2:A13)"), ("J3", "=H3-I3"),
                          ("H4", "=SUM(E2:E4)"), ("I4", "=SUM(Tasks!G2:G13)"), ("J4", "=H4-I4")]:
        s[cell] = formula
    s["I4"].number_format = RM
    s["J4"].number_format = RM
    s["A7"] = "Finding: 4 tasks in each status; 12 tasks in total."
    s["A8"] = "Finding: Procurement has the largest planned total: RM4,000 of RM10,400."
    widths(s, D=20, E=18, G=18)

    tests = duplicate(wb, s, "Chart Range Tests")
    summary_charts(s)
    summary_charts(tests)

    log = wb.create_sheet("Summary Test Log")
    put(log, "A1", blocks(6, "6.9")[0])
    widths(log, A=18, B=36, C=44, D=40)
    wrap(log, "A1:D8")
    names = wb.sheetnames
    names.remove("Summary Test Log")
    names.remove("Chart Range Tests")
    names += ["Summary Test Log", "Chart Range Tests"]
    order(wb, names)


def lab07(wb):
    reg = duplicate(wb, wb["Tasks"], "Register Output")
    reg.delete_cols(10, 30)
    reg.delete_rows(14, 50)
    reg.freeze_panes = "A2"

    plan = wb.create_sheet("Output Plan")
    put(plan, "A1", blocks(7, "7.4")[0])
    b9 = blocks(7, "7.9")
    put(plan, "B9", b9[0])
    put(plan, "A12", b9[1])
    widths(plan, A=26, B=100)
    wrap(plan, "B1:B17")
    names = [n for n in wb.sheetnames if n not in ("Register Output", "Output Plan")]
    order(wb, names[:1] + ["Register Output", "Output Plan"] + names[1:])


STEPS = [lab01, lab02, lab03, lab04, lab05, lab06, lab07]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for n in range(1, len(STEPS) + 1):
        # Build each file from the starter: openpyxl can't read charts back in.
        wb = openpyxl.load_workbook(ROOT / "shared/sample-files/TaskRegister.xlsx")
        for step in STEPS[:n]:
            step(wb)
        path = OUT / f"GW-Sheets-start-Lab{n + 1:02d}.xlsx"
        wb.save(path)
        print(f"  {path.relative_to(ROOT)}: {', '.join(wb.sheetnames)}")


if __name__ == "__main__":
    main()
