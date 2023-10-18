from PIL import Image, ImageDraw, ImageFont, ImageFilter
import datetime
from functions import TeamCheck

EventName = "Champions LA"
date_now = datetime.datetime.now()
Date = str(date_now.strftime('%Y年%m月%d日 %H:%M:%S～'))
out = "../out/match_Image.jpg"
out_vote = "../out/vote_Image.jpg"

font_Valorant = ImageFont.truetype("../resource/font/Valorant Font.ttf", 90)
font_Myrica = ImageFont.truetype("../resource/font/Myrica.TTC", 80)
font_Myrica_Small = ImageFont.truetype("../resource/font/Myrica.TTC", 70)
font_Valorant_mini = ImageFont.truetype("../resource/font/Valorant Font.ttf", 70)

def MkImage(NameEvent, month, day, hour, minutes, T1, T2):
    
    team1, team2 = TeamCheck.TeamCheck(T1, T2)
        
    Date = str(month).rjust(2, "0") + "月" + str(day).rjust(2, "0") + "日　" + str(hour).rjust(2, "0") + ":" + str(minutes).rjust(2, "0") + "～"
        
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
    
    
    draw.text((960, 150), NameEvent, "#ffffff", font=font_Myrica, anchor='md')
    draw.text((960, 300), Date, "#ffffff", font=font_Myrica, anchor='md')
    if T1 == "dfm":
        draw.text((480, 950), team1[2], "#ffffff", font=font_Valorant_mini, anchor='md')
    else:
        draw.text((480, 950), team1[2], "#ffffff", font=font_Valorant, anchor='md')
    if T2 == "dfm":
        draw.text((1440, 950), team2[2], "#ffffff", font=font_Valorant_mini, anchor='md')
    else:
        draw.text((1440, 950), team2[2], "#ffffff", font=font_Valorant, anchor='md')
    
    
    
    print(img_back.format, img_back.size, img_back.mode)

    #img_back.show()
    
    img_back.save(out)
    
def MkVote(color, T1, T2):
    
    #img_back_ascention = Image.open('../resource/Image/Vote_back_ascention.jpg')
    #img_back_challengers = Image.open('../resource/Image/Vote_back_challengers.jpg')
    #img_back_kickoff = Image.open('../resource/Image/Vote_back_kickoff.jpg')
    
    img_back = Image.open(TeamCheck.ImgCheck(color))
    
    team1, team2 = TeamCheck.TeamCheck(T1, T2)
    img_team1 = Image.open(team1[0])
    img_team2 = Image.open(team2[1])
    
    team1_cp = img_team1.copy()
    team1_cp.thumbnail((800, 800))
    team2_cp = img_team2.copy()
    team2_cp.thumbnail((800, 800))
    
    img_back.paste(team1_cp, (100, 300), team1_cp)
    img_back.paste(team2_cp, (1000, 300), team2_cp)
    
    draw = ImageDraw.Draw(img_back)
    
    draw.text((450, 975), team1[2], "#000000", font=font_Myrica_Small, anchor='md')
    draw.text((1470, 975), team2[2], "#000000", font=font_Myrica_Small, anchor='md')
    
    img_back.save(out_vote)