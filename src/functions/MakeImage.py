from PIL import Image, ImageDraw, ImageFont, ImageFilter
import datetime

EventName = "Champions LA"
date_now = datetime.datetime.now()
Date = str(date_now.strftime('%Y年%m月%d日 %H:%M:%S~'))
out = "../out/match_Image.jpg"

font_Valorant = ImageFont.truetype("../resource/font/Valorant Font.ttf", 100)
font_Myrica = ImageFont.truetype("../resource/font/Myrica.TTC", 80)

fnc = ["../resource/Image/fnc_logo_left.png", "../resource/Image/fnc_logo_right.png", "Fnatic"]
prx = ["../resource/Image/prx_logo_left.png", "../resource/Image/prx_logo_right.png", "Paper Rex"]
zeta = ["../resource/Image/zeta_logo_left.png", "../resource/Image/zeta_logo_right.png", "ZETA DIVISION"]

team1 = fnc
team2 = prx

def MkImage():
    img_back = Image.open('../resource/Image/Match_back.jpg')
    img_team1 = Image.open(team1[0])
    img_team2 = Image.open(team2[1])
    
    team1_cp = img_team1.copy()
    team1_cp.thumbnail((800, 800))
    team2_cp = img_team2.copy()
    team2_cp.thumbnail((800, 800))
    
    draw = ImageDraw.Draw(img_back)
    
    img_back.paste(team1_cp, (100, 300), team1_cp)
    img_back.paste(team2_cp, (1000, 300), team2_cp)
    
    
    draw.text((960, 150), EventName, "#ffffff", font=font_Myrica, anchor='md')
    draw.text((960, 300), Date, "#ffffff", font=font_Myrica, anchor='md')
    draw.text((480, 950), team1[2], "#ffffff", font=font_Valorant, anchor='md')
    draw.text((1440, 950), team2[2], "#ffffff", font=font_Valorant, anchor='md')
    
    
    
    print(img_back.format, img_back.size, img_back.mode)

    img_back.show()
    
    img_back.save(out)