from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
root=Path(__file__).resolve().parents[1]

# Colours and type follow training-book-kit BRAND.md: navy titles, plain purple numerals,
# white cards with thin grey rules on a near-white background, teal connectors.
NAVY,PURPLE,TEAL,GREY,RULE,BG='#1E2761','#6B5DD3','#028090','#616161','#E0E0E0','#F8F9FC'
stages=[('01','Prepare','Workspace and sources'),('02','Draft','Checked brief'),('03','Coordinate','Meeting and actions'),('04','Track','Reporting dashboard'),('05','Present','Sponsor update'),('06','Hand over','Project hub')]
im=Image.new('RGB',(1600,430),BG);d=ImageDraw.Draw(im)

# Segoe UI on Windows; Inter or DejaVu where Segoe UI isn't installed.
FONTS={'regular':['C:/Windows/Fonts/segoeui.ttf','/usr/share/fonts/opentype/inter/Inter-Regular.otf','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'],
       'semibold':['C:/Windows/Fonts/seguisb.ttf','/usr/share/fonts/opentype/inter/Inter-SemiBold.otf','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'],
       'light':['C:/Windows/Fonts/segoeuil.ttf','/usr/share/fonts/opentype/inter/Inter-Light.otf','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf']}
def font(size,weight='regular'):
 for path in FONTS[weight]:
  if Path(path).exists(): return ImageFont.truetype(path,size)
 raise SystemExit('No usable font found for '+weight)

d.text((48,30),'Your Google Workspace training journey',font=font(32,'semibold'),fill=NAVY)
d.text((48,82),'One fictional reporting pilot. Six practical stages.',font=font(23),fill=GREY)
for i,(num,title,desc) in enumerate(stages):
 x=48+i*251
 d.rounded_rectangle((x,148,x+232,352),radius=12,fill='white',outline=RULE,width=2)
 d.text((x+20,160),num,font=font(46,'light'),fill=PURPLE)
 d.text((x+20,232),title,font=font(23,'semibold'),fill=NAVY)
 words=desc.split(); lines=[]; line=''
 for word in words:
  if d.textlength((line+' '+word).strip(),font=font(19))>192: lines.append(line);line=word
  else: line=(line+' '+word).strip()
 lines.append(line)
 for j,l in enumerate(lines): d.text((x+20,272+j*25),l,font=font(19),fill=GREY)
 if i<5:
  # A short teal arrow in the gap between cards.
  y=250; d.line((x+235,y,x+247,y),fill=TEAL,width=3); d.polygon([(x+249,y),(x+243,y-5),(x+243,y+5)],fill=TEAL)
d.text((48,380),'Masterclass: follow the workflow. Specialist courses: practise each application in more depth.',font=font(20),fill=GREY)
im.save(root/'program-flow.png',optimize=True)
