fnc = ["../resource/Image/tier1/fnc_logo_left.png", "../resource/Image/tier1/fnc_logo_right.png", "Fnatic"]
prx = ["../resource/Image/tier1/prx_logo_left.png", "../resource/Image/tier1/prx_logo_right.png", "Paper Rex"]
zeta = ["../resource/Image/tier1/zeta_logo_left.png", "../resource/Image/tier1/zeta_logo_right.png", "ZETA DIVISION"]
eg = ["../resource/Image/tier1/eg_logo_left.png", "../resource/Image/tier1/eg_logo_right.png", "Evil Geniuses"]
drx = ["../resource/Image/tier1/drx_logo_left.png", "../resource/Image/tier1/drx_logo_right.png", "DRX"]
loud = ["../resource/Image/tier1/loud_logo_left.png", "../resource/Image/tier1/loud_logo_right.png", "LOUD"]
ht = ["../resource/Image/tier1/100t_logo_left.png", "../resource/Image/tier1/100t_logo_right.png", "100 Thieves"]
c9 = ["../resource/Image/tier1/c9_logo_left.png", "../resource/Image/tier1/c9_logo_right.png", "Cloud9"]
edg = ["../resource/Image/tier1/edg_logo_left.png", "../resource/Image/tier1/edg_logo_right.png", "Edward Gaming"]
navi = ["../resource/Image/tier1/navi_logo_left.png", "../resource/Image/tier1/navi_logo_right.png", "Natus Vincere"]
tl = ["../resource/Image/tier1/tl_logo_left.png", "../resource/Image/tier1/tl_logo_right.png", "Team Liquid"]
nrg = ["../resource/Image/tier1/nrg_logo_left.png", "../resource/Image/tier1/nrg_logo_right.png", "NRG"]

sz = ["../resource/Image/tier2/sz_logo_left.png", "../resource/Image/tier2/sz_logo_right.png", "SCARZ"]
fl = ["../resource/Image/tier2/fl_logo_left.png", "../resource/Image/tier2/fl_logo_right.png", "FENNEL"]

challengers = 0x0db397
ascention = 0x0d9093
GC = 0xe09600
kickoff = 0xc01106
emea = 0xdc3030
americas = 0xff570c
pacific = 0x01d2d7
china = 0xebcd43
masters = 0x6f4acc
champions = 0xc5b174

img_back_ascention = '../resource/Image/Vote_back_ascention.jpg'
img_back_challengers = '../resource/Image/Vote_back_challengers.jpg'
img_back_gc = '../resource/Image/Vote_back_gc.jpg'
img_back_kickoff = '../resource/Image/Vote_back_kickoff.jpg'
img_back_emea = '../resource/Image/Vote_back_emea.jpg'
img_back_americas = '../resource/Image/Vote_back_americas.jpg'
img_back_pacific = '../resource/Image/Vote_back_pacific.jpg'
img_back_china = '../resource/Image/Vote_back_china.jpg'
img_back_masters = '../resource/Image/Vote_back_masters.jpg'
img_back_champions = '../resource/Image/Vote_back_champions.jpg'


def TeamCheck(team1, team2):
    if team1 == "fnc":
        team1 = fnc
    elif team1 == "prx":
        team1 = prx
    elif team1 == "zeta":
        team1 = zeta
    elif team1 == "eg":
        team1 = eg
    elif team1 == "drx":
        team1 = drx
    elif team1 == "loud":
        team1 = loud
    elif team1 == "100t":
        team1 = ht
    elif team1 == "c9":
        team1 = c9
    elif team1 == "edg":
        team1 = edg
    elif team1 == "navi":
        team1 = navi
    elif team1 == "tl":
        team1 = tl
    elif team1 == "nrg":
        team1 = nrg
    elif team1 == "sz":
        team1 = sz
    elif team1 == "fl":
        team1 = fl
        
    
    if team2 == "fnc":
        team2 = fnc
    elif team2 == "prx":
        team2 = prx
    elif team2 == "zeta":
        team2 = zeta
    elif team2 == "eg":
        team2 = eg
    elif team2 == "drx":
        team2 = drx
    elif team2 == "loud":
        team2 = loud
    elif team2 == "100t":
        team2 = ht
    elif team2 == "c9":
        team2 = c9
    elif team2 == "edg":
        team2 = edg
    elif team2 == "navi":
        team2 = navi
    elif team2 == "tl":
        team2 = tl
    elif team2 == "nrg":
        team2 = nrg
    elif team2 == "sz":
        team2 = sz
    elif team2 == "fl":
        team2 = fl
    
    return team1, team2

def color(text):
    
    if text == "challengers":
        return challengers
    elif text == "ascention":
        return ascention
    elif text == "gc":
        return GC
    elif text == "kickoff":
        return kickoff
    elif text == "emea":
        return emea
    elif text == "americas":
        return americas
    elif text == "pacific":
        return pacific
    elif text == "china":
        return china
    elif text == "masters":
        return masters
    elif text == "champions":
        return champions
    
def ImgCheck(text):
    if text == "challengers":
        return img_back_challengers
    elif text == "ascention":
        return img_back_ascention
    elif text == "gc":
        return img_back_gc
    elif text == "kickoff":
        return img_back_kickoff
    elif text == "emea":
        return img_back_emea
    elif text == "americas":
        return img_back_americas
    elif text == "pacific":
        return img_back_pacific
    elif text == "china":
        return img_back_china
    elif text == "masters":
        return img_back_masters
    elif text == "champions":
        return img_back_champions
    
def Channel(text):
    if text == "announce":
        return 0
    else:
        return 1