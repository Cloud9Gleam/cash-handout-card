from PIL import Image, ImageDraw, ImageFont
W,H=1050,600
B="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
R="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
def F(p,s): return ImageFont.truetype(p,s)
def center(d,y,text,font,fill=0):
    w=d.textlength(text,font=font); d.text(( (W-w)/2, y), text, font=font, fill=fill)
# FRONT
img=Image.new("L",(W,H),255); d=ImageDraw.Draw(img)
d.rectangle([18,18,W-19,H-19],outline=0,width=6)
d.rectangle([34,34,W-35,H-35],outline=0,width=2)
# coin graphic top center
cx,cy,rad=W//2,150,72
d.ellipse([cx-rad,cy-rad,cx+rad,cy+rad],outline=0,width=7)
d.ellipse([cx-rad+14,cy-rad+14,cx+rad-14,cy+rad-14],outline=0,width=2)
center(d,cy-38,"$",F(B,72))
center(d,268,"CASH IS FREEDOM",F(B,64))
d.line([200,360,850,360],fill=0,width=4)
for i,line in enumerate(["Private  •  Fungible  •  Offline","No bank needed. No tracking."]):
    center(d,385+i*48,line,F(B,30))
center(d,505,"It works when the power goes out.",F(R,28))
img.save("/tmp/card_front.png"); img.convert("1").save("/home/hatch/workspace/taskmarket/poidh-1510/card_front.png")
# BACK
img=Image.new("L",(W,H),255); d=ImageDraw.Draw(img)
d.rectangle([18,18,W-19,H-19],outline=0,width=6)
d.rectangle([34,34,W-35,H-35],outline=0,width=2)
center(d,58,"WHY CASH MATTERS",F(B,52))
d.line([200,140,850,140],fill=0,width=4)
lines=["Every card tap leaves a trail:","where you were, what you bought,","who you paid. Cash leaves none.","Cash is yours to hold, spend,","and give — no permission,","no account, no shutdown switch."]
y=175
for ln in lines:
    center(d,y,ln,F(R,32)); y+=44
d.rectangle([180,440,870,505],fill=0)
center(d,455,"PAY CASH. KEEP CASH ALIVE.",F(B,32),fill=255)
center(d,520,"Use it. Ask for it. Accept it.",F(R,24))
img.save("/tmp/card_back.png"); img.convert("1").save("/home/hatch/workspace/taskmarket/poidh-1510/card_back.png")
print("done")
