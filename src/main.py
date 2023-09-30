import discord
from discord import app_commands
from functions import MakeImage
from functions import TeamCheck
from discord.utils import get
import config

#【祝】共同開発者一名増員！！！

TOKEN = config.VCTUDB_TOKEN

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

channel_vote = 1156883149880574083  #勝利予想チャンネル
channel_test = 1126294770210312255  #自鯖チャンネル
channnel_bot = 1153702899390623871  #bot実験場
channel_team1 = 1157193592226463846 #チーム１VC
channel_team2 = 1157193592226463846 #チーム２VC

one_emoji = "1️⃣"
two_emoji = "2️⃣"

@client.event

async def on_ready():
    
    print("起動したぜ～^-^)v")
    
    await tree.sync()
    
async def on_raw_reaction_add(payload):
    
    channel = client.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    reaction = get(message.reactions, emoji=payload.emoji.name)
    
    if channel == channel_vote:
        if payload.emoji_name == one_emoji:
            team1_num = reaction.count - 1
            team1_name = "チーム１投票数：" + str(team1_num)
        elif payload.emoji_name == two_emoji:
            team2_num = reaction.count - 1
            team2_name = "チーム２投票数：" + str(team2_num)
        
        await channel_team1.edit(name=team1_name)
        await channel_team2.edit(name=team2_name)
        
@tree.command(name="add-match", description="Make Image of match(Admin only)")
@app_commands.rename(title="大会名", team1="チーム1", team2="チーム2")

async def addMatch_command(interaction: discord.Interaction, title: str, month: int, day: int, hour: int, minutes: int, team1: str, team2: str):
   
    MakeImage.MkImage(title, month, day, hour, minutes, team1, team2)
    
    file = discord.File("../out/match_Image.jpg", filename = "match_Image.jpg")
    embed=discord.Embed(title="Image", color=0xff0000)
    embed.set_image(url="attachment://match_Image.jpg")
    
    await interaction.channel.send(file=file, embed=embed)
    #await interaction.response.send_message(file="../out/match_Image.jpg")
    
@tree.command(name="vote_img", description="勝利するチームを予想しよう！")

async def vote_command(interaction: discord.Interaction, color: str, metatitle: str, team1: str, team2: str):
    
    T1, T2 = TeamCheck.TeamCheck(team1, team2)
    
    MakeImage.MkVote(color, team1, team2)
    file = discord.File("../out/vote_Image.jpg", filename = "vote_Image.jpg")
    Color = TeamCheck.color(color)
    channel = client.get_channel(channel_vote)
    Event_title = str(metatitle) + "勝利予想！"
    embed = discord.Embed(title= Event_title, description=str(metatitle) + "の勝利チームを予想しよう！", color=Color)
    embed.add_field(name="投票方法", value=str(T1[2]) + "は :one: \n" + str(T2[2] + "は :two: \nのリアクションで投票！"))
    embed.set_image(url="attachment://vote_Image.jpg")
    
    msg = await channel.send(file=file, embed=embed)
    await msg.add_reaction(one_emoji)
    await msg.add_reaction(two_emoji)
    
client.run(TOKEN)