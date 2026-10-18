from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
root=Path(__file__).resolve().parents[1]

stages=[('01','PREPARE','Workspace and sources'),('02','DRAFT','Checked brief'),('03','COORDINATE','Meeting and actions'),('04','TRACK','Reporting dashboard'),('05','PRESENT','Sponsor update'),('06','HAND OVER','Project hub')]
im=Image.new('RGB',(1600,430),'#f3f6fb');d=ImageDraw.Draw(im)
def font(size,bold=False):
 return ImageFont.truetype('C:/Windows/Fonts/'+('arialbd.ttf' if bold else 'arial.ttf'),size)
d.text((48,32),'YOUR GOOGLE WORKSPACE TRAINING JOURNEY',font=font(31,True),fill='#183153')
d.text((48,83),'One fictional reporting pilot. Six practical stages.',font=font(23),fill='#53657d')
colours=['#1967d2','#188038','#9334e6','#188038','#b06000','#1967d2']
for i,(num,title,desc) in enumerate(stages):
 x=48+i*251
 d.rounded_rectangle((x,153,x+232,351),radius=16,fill='white',outline='#d6dfeb',width=2)
 d.rounded_rectangle((x+18,172,x+69,216),radius=9,fill=colours[i])
 d.text((x+26,179),num,font=font(25,True),fill='white')
 d.text((x+18,238),title,font=font(21,True),fill='#183153')
 words=desc.split(); lines=[]; line=''
 for word in words:
  if d.textlength((line+' '+word).strip(),font=font(19))>196: lines.append(line);line=word
  else: line=(line+' '+word).strip()
 lines.append(line)
 for j,l in enumerate(lines): d.text((x+18,278+j*25),l,font=font(19),fill='#53657d')
 if i<5:d.text((x+237,235),'>',font=font(22,True),fill='#879bb5')
d.text((48,382),'Masterclass: follow the workflow. Specialist courses: practise each application in more depth.',font=font(20),fill='#53657d')
im.save(root/'program-flow.png',optimize=True)
