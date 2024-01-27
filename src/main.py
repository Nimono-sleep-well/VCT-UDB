import discord
from discord import app_commands
from functions import (
    MakeImage,
    TeamCheck
)
import config
import json
import datetime

TOKEN = config.VCTUDB_TOKEN

# MYID = config.MY_ID
MYID = 790521229639286804

date_now = datetime.datetime.now()
Date = str(date_now.strftime('%Y/%m/%d %h:%m'))

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

file_roaster = "../resource/text/team_roaster/Roaster.json"

channel_announce = 1153604048264646728
channel_rules = 1153599232301858837  # rules
channel_vote = 1169623561145679982  # 勝利予想チャンネル
channel_test = 1126294770210312255  # 自鯖チャンネル
channel_bot = 1153702899390623871  # bot実験場
channel_dash = 1159847883642785952  # ダッシュボード

one_emoji = "1️⃣"
two_emoji = "2️⃣"
red_emoji = "🔴"
blue_emoji = "🔵"


@client.event
async def on_ready():
    print("起動したぜ～^-^)v")

    await tree.sync()


@tree.command(name="add-match", description="/add-match [title] [team1] [team2]")
@app_commands.rename(title="大会名", team1="チーム1", team2="チーム2")
async def addMatch_command(interaction: discord.Interaction, title: str, month: int, day: int, hour: int, minutes: int,
                           team1: str, team2: str):
    if interaction.user.id == MYID:
        MakeImage.MkImage(title, month, day, hour, minutes, team1, team2)

        file = discord.File("../out/match_Image.jpg", filename="match_Image.jpg")
        embed = discord.Embed(title="Image", color=0xff0000)
        embed.set_image(url="attachment://match_Image.jpg")

        await interaction.channel.send(file=file)
        # await interaction.response.send_message(file="../out/match_Image.jpg")
    else:
        await interaction.response.send_message("管理者権限がないため，このコマンドを実行できません", ephemeral=True)


@tree.command(name="vote_img", description="/vote_img [title] [metatitle] [team1] [team2]")
async def vote_command(interaction: discord.Interaction, color: str, metatitle: str, team1: str, team2: str):
    if interaction.user.id == MYID:
        T1, T2 = TeamCheck.TeamCheck(team1, team2)

        MakeImage.MkVote(color, team1, team2)
        file = discord.File("../out/vote_Image.jpg", filename="vote_Image.jpg")
        color_ = TeamCheck.color(color)
        channel = client.get_channel(channel_vote)
        dash = client.get_channel(channel_dash)
        event_title = str(metatitle) + "勝利予想！"
        msg_ = dash.fetch_message(1169630810815598743)

        embed = discord.Embed(title=event_title, description=str(metatitle) + "の勝利チームを予想しよう！", color=color_)
        embed.add_field(name="投票方法",
                        value=str(T1[2]) + "は :one: \n" + str(T2[2] + "は :two: \nのリアクションで投票！"))
        embed.set_image(url="attachment://vote_Image.jpg")

        embed2 = discord.Embed(title="投票状況", description=T1[2] + "vs" + T2[2])
        embed2.add_field(name=red_emoji + T1[2], value="[--%]")
        embed2.add_field(name=blue_emoji + T2[2], value="[--%]")
        embed2.add_field(name="`[----------]`", value="", inline=False)
        embed2.add_field(name="", value=Date, inline=False)

        msg = await channel.send(file=file, embed=embed)
        await msg.add_reaction(one_emoji)
        await msg.add_reaction(two_emoji)
        await msg_.edit(embed=embed2)
    else:
        await interaction.response.send_message("管理者権限がないため，このコマンドを実行できません", ephemeral=True)


@tree.command(name="roaster", description="ロスター表示")
async def roaster_command(interaction: discord.Interaction, team: str):
    TEAM = TeamCheck.RoasterCheck(team)
    with open(file_roaster) as f:
        roaster = json.load(f)

        info = roaster[team]
        last_change = roaster["last_change"]

        player = "\n".join(info["player"])
        coach = "\n".join(info["coach"])
        analyst = "\n".join(info["analyst"])

        file = discord.File(TEAM[1], filename="team_logo.png")

        embed = discord.Embed(title="ロスター情報", description=TEAM[2] + "のロスター情報です", color=TEAM[3])
        embed.add_field(name="Player:", value=player)
        embed.add_field(name="Coach:", value=coach)
        embed.add_field(name="Analyst:", value=analyst)
        embed.add_field(name="", value="```最終更新:" + last_change + "```", inline=False)
        embed.set_thumbnail(url="attachment://team_logo.png")
    await interaction.channel.send(file=file, embed=embed)


@tree.command(name="transfer", description="/transfer [team2/none] [player] [description/none]")
async def transfer_command(interaction: discord.Interaction, team1: str, team2: str, member: str, description: str):
    TEAM1 = TeamCheck.RoasterCheck(team1)
    TEAM2 = TeamCheck.RoasterCheck(team2)
    with open(file_roaster) as f:
        roaster = json.load(f)

        info = roaster[team1]

        last_change = roaster["last_change"]

        player = "\n".join(info["player"])
        coach = "\n".join(info["coach"])
        analyst = "\n".join(info["analyst"])

        file = discord.File(TEAM1[1], filename="team_logo.png")

        embed = discord.Embed(title=member + " joined " + TEAM1[2] + "!",
                              description="元 " + TEAM2[2] + " の " + member + " が " + TEAM1[2] + " に加入しました",
                              color=TEAM1[3])
        embed.add_field(name=TEAM1[2] + "'s New Roaster", value="", inline=False)
        embed.add_field(name="Player:", value=player)
        embed.add_field(name="Coach:", value=coach)
        embed.add_field(name="Analyst:", value=analyst)
        embed.add_field(name="説明", value=description)
        embed.add_field(name="", value="```最終更新:" + last_change + "```", inline=False)
        embed.set_thumbnail(url="attachment://team_logo.png")
    await interaction.channel.send(file=file, embed=embed)


@tree.command(name="news", description="/news [description] [url]")
async def news_command(interaction: discord.Interaction, title: str, description: str, url: str):
    embed = discord.Embed(title=title, description=description)
    embed.add_field(name="", value=url)
    await interaction.channel.send(embed=embed)


@tree.command(name="winner", description="/vote_info [team1] [team2]")
async def winner_command(interaction: discord.Interaction, num: str, name_map: str, team: str):
    if interaction.user.id == MYID:

        team = TeamCheck.RoasterCheck(team)

        text = "## Riot Games ONE 第" + num + "試合 " + name_map + "\n # " + team[2] + " 勝利！！"

        await interaction.channel.send(text)

    else:
        await interaction.response.send_message("管理者権限がないため，このコマンドを実行できません", ephemeral=True)
        
@tree.command(name="send", description="/send")
async def send_command(interaction: discord.Interaction):
    title = "Riot Games ONE 結果発表"
    description = "2023/12/03～04にかけて行われた，Riot Games ONE PRO INVITATIONALの結果発表です。"
    embed = discord.Embed(title=title, description = description)
    embed.addfield(name="優勝：Natus Vincere")
    embed.addfield(name="第二位：ZETA DIVISION")
    embed.addfield(name="第三位：Bleed eSports")
    embed.addfield(name="第四位：DetonatioN FocusMe")
    
    await interaction.channel.send(embed=embed)


client.run(TOKEN)
