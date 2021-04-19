import discord
from discord.ext import commands
import random
import datetime
import wikipedia
import time
import json

#For help command
cmd1="help<page>";cmd2="doge";cmd3="ping";cmd4="kill <name>";cmd5="time";cmd6="calc <x><operator><y>";cmd7="pokechart";cmd8="wiki <search term>";cmd9="ki";cmd10="ship";cmd11="bg";cmd12="meme"
cmd13="dice";cmd14="num <min> <max>";cmd15="waifu";cmd16="spam <user> <amount> <msg>";cmd17="anon <user> <message>";cmd18="shout <message>";cmd19="rps <choice>";cmd20="link"
des1="You're already here!";des2="Displays a friendly doge.";des3="Finds latency of bot.";des4="Kills a person of your choice.";des5="Displays the current time.(24hour format)"
des6="Does math for you.(Currently toggled off)";des7="Displays a chart of pokemon types.";des8="Finds wikipedia summaries.";des9="Just a pretty ki command.";des10="Displays a random ship."
des11="Displays a nice view.";des12="Displays a random meme template.";des13="Rolls a standard 6-sided dice.";des14="Displays number between <min> & <max>."
des15="Displays a random waifu **uwu**";des16="Spams a person of your choice?";des17="Anonymously DMs a person of your choice.";des18="Makes your message stand out.";des19="Plays Rock Paper Scissors against me!"
des20="Sends the invite link for this bot."
#defaultans
ans = ["Badaki!","Kiiii!!","Ohpeee!","I hate this now!!!","This is illegal!!"]


client = commands.Bot(command_prefix = "%",case_insensitive=True)
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,activity=discord.Game("piano | %help"))
    print("Bot Activated.")

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("**Invalid Request!**\nPlease input all necessary arguments.")

#command1//help
@client.command(aliases = ["help","info","help1"])
async def _help(ctx):
    embed = discord.Embed(
        title="Help(1)",
        description="Type %help2 for more commands."
    )
    embed.add_field(name="Command:",value=cmd1+"\n"+cmd2+"\n"+cmd3+"\n"+cmd4+"\n"+cmd5+"\n"+cmd6+"\n"+cmd7+"\n"+cmd8+"\n"+cmd9+"\n"+cmd10+"\n"+cmd11+"\n"+cmd12,inline=True)
    embed.add_field(name="Description:",value=des1+"\n"+des2+"\n"+des3+"\n"+des4+"\n"+des5+"\n"+des6+"\n"+des7+"\n"+des8+"\n"+des9+"\n"+des10+"\n"+des11+"\n"+des12,inline=True)
    await ctx.send(embed=embed)
@client.command(aliases = ["help2","info2"])
async def _help2(ctx):
    embed = discord.Embed(
        title="Help(2)",
        description="Type %help1 for more commands."
    )
    embed.add_field(name="Command:",value=f"{cmd13}\n{cmd14}\n{cmd15}\n{cmd16}\n{cmd17}\n{cmd18}\n{cmd19}\n{cmd20}")
    embed.add_field(name="Description:",value=f"{des13}\n{des14}\n{des15}\n{des16}\n{des17}\n{des18}\n{des19}\n{des20}")
    await ctx.send(embed=embed)
#command2//doge
@client.command()
async def doge(ctx):
    await ctx.send("░▄▀▄▀▀▀▀▄▀▄░░░░░░░░░\n░█░░░░░░░░▀▄░░░░░░▄░\n█░░▀░░▀░░░░░▀▄▄░░█░█\n█░▄░█▀░▄░░░░░░░▀▀░░█\n█░░▀▀▀▀░░░░░░░░░░░░█\n█░░░░░░░░░░░░░░░░░░█\n█░░░░░░░░░░░░░░░░░░█\n░█░░▄▄░░▄▄▄▄░░▄▄░░█░\n░█░▄▀█░▄▀░░█░▄▀█░▄▀░\n░░▀░░░▀░░░░░▀░░░▀░░░")                   
#command3//ping
@client.command()
async def ping(ctx):
    await ctx.send(f"{round(client.latency * 1000)}ms")
#command4//kill
@client.command(aliases = ["attack","kill"])
async def _kill(ctx,target):
    deathchoices = ["got stabbed", "was brutally choked", "was eaten by wolves", "fell down a flight of stairs", "died to a light tap on the shoulder", "was effectively eliminated",
                    "left life's servers","took an L","mysteriously disappeared","needed some milk","aged too fast","melted into a puddle","overdosed on air","no longer exists",
                    "decided to visit their great-great-great grandparents","was Thanos snapped out of existence","wa mou shindeiru"]
    if target == "<@!708053835704172574>" or target == "<@!155727989055684608>":
        rand = random.randint(1,2)
        if rand == 1:
            unoreverse = ctx.message.author.mention
            await ctx.send("***Pulls out uno reverse card***")
            time.sleep(1)
            await ctx.send("**Omae wa mou shindeiru.**")
            time.sleep(1)
            await ctx.send(f"{unoreverse} {random.choice(deathchoices)}.")
        elif rand == 2:
            await ctx.send(f"{target} {random.choice(deathchoices)}.")
            time.sleep(1)
            await ctx.send("Wait a sec...")
            time.sleep(1)
            await ctx.send(f"Oh no! {random.choice(ans)}")
    else:
        await ctx.send(f"{target} {random.choice(deathchoices)}.")
#command5//time
@client.command(aliases = ["time", "now", "currenttime", "current", "t"])
async def _time(ctx):
    currenttime = datetime.datetime.now()
    await ctx.send(currenttime.strftime("**%B %d, %Y**\n%H:%M"))
#command6//calc
#@client.command(aliases = ["calculate", "calc"])
#async def _calc(ctx, expr):
#    try:
#        await ctx.send(str(numexpr.evaluate(expr).item()))
#    except SyntaxError:
#        await ctx.send("Please enter the correct syntax.")
#command7//weak
@client.command(aliases = ["weak","weakness","resistances","resist","pokechart","poketypes","types","strengths","strength"])
async def _weak(ctx):
    embed = discord.Embed(
        title="Pokemon Strengths/Weaknesses/Resistances Chart",
        description="Y-Axis = Attacking Move Type; X-Axis = Defender's Type(s)\nFor a defender with 2 types, multiply damage multipliers for both types individually. Ex: Normal type attacking move VS Rock + Steel type defender = 0.5 x 0.5 damage multiplier = 0.25x damage multiplier."
    )
    embed.set_image(url="https://assets.vg247.com/current/2019/11/pokemon_sword_shield_type_chart_strengths_weakness_effectiveness_resistance.jpg")
    embed.set_footer(text="Click Image to Enlarge")
    await ctx.send(embed=embed)
#command8//wiki
@client.command(aliases = ["wiki","wikipedia","search","google","summary"])
async def _wiki(ctx,userinput):
    wikititle=(wikipedia.page(userinput).title)
    embed = discord.Embed(
        title=f"Search Results for {userinput}:",
        description=(wikipedia.summary(wikititle))
    )
    embed.set_footer(text=f"https://en.wikipedia.org/wiki/{wikititle}")
    await ctx.send(embed=embed)
#command9//ki
@client.command(aliases = ["ki"])
async def _ki(ctx):
    answers = ["Badaki!","Kiiiiii","Ohpe!","Oops! I hate this now!!!","No u!","Wakayyy!"]
    await ctx.send(f"{random.choice(answers)}")
#command10//ship
@client.command(aliases = ["ship","relationship"])
async def _ship(ctx):
    defaultships = ["**Rebill**","**Nianen**","Kill","Jai","Rai","Kalden","Brose","Kiwan","Rowan","A Randular Bot","Cabutt","Kabutt","Benee","Haha I'm alone","Lucalynn","Weeb + Weeb = True Love",
                    "Benlynn"]
    rand = random.choice(defaultships)
    await ctx.send(f"{rand} :heart:")
    if rand == "**Nianen**" or rand == "Benee" or rand == "Haha I'm alone" or rand == "Benlynn":
        time.sleep(1)
        await ctx.send("Wait a sec...")
        time.sleep(1)
        await ctx.send(f"Oh no! {random.choice(ans)}")
#command11//bg
@client.command(aliases = ["background","bg"])
async def _bg(ctx):
    bg = open("backgrounds.txt","r")
    bgcontent = bg.read()
    bgsplit = bgcontent.split("\n")
    realrand = random.choice(bgsplit)
    embed = discord.Embed()
    embed.set_image(url=str(realrand))
    embed.set_footer(text=f"Courtesy:\n{realrand}")
    await ctx.send(embed=embed)
    bg.close()
#command12//meme
@client.command()
async def meme(ctx):
    memes = open("meme urls.txt","r")
    memelist = memes.read()
    memesplit = memelist.split("\n")
    rand = random.choice(memesplit)
    embed = discord.Embed()
    embed.set_image(url=str(rand))
    await ctx.send(embed=embed)
#command13//dice
@client.command()
async def dice(ctx):
    rand = random.randint(1,6)
    await ctx.send(file=discord.File(f"{rand}dice.png"))
    await ctx.send(f"You rolled a {rand}!")
#command14//number
@client.command(aliases = ["number","randnumber","randomnumber","num"])
async def _num(ctx,num1,num2):
    rand = random.randint(int(num1),int(num2))
    await ctx.send(rand)
#command15//waifu
@client.command(aliases = ["waifu","anime"])
async def _waifu(ctx):
    waifus = open("waifus.txt","r")
    waifucontent = waifus.read()
    waifusplit = waifucontent.split("\n")
    randwaifu = random.choice(waifusplit)
    embed = discord.Embed()
    embed.set_image(url=str(randwaifu))
    await ctx.send(embed=embed)
    waifus.close()
#command16//spam
@client.command()
async def spam(ctx, foo, amount, foo2):
    for x in range(int(amount)):
        if int(amount) > 100:
            await ctx.send("For the sake of the one getting spammed, spam amount is capped at 100.")
            break
        await ctx.author.send(f"<@!{str(ctx.author.id)}> No u lol.")
#command17//dm
@client.command(aliases = ["anon","msg","dm","message"])
async def _dm(ctx, member: discord.Member, *message):
    channel = await member.create_dm()
    await channel.send(" ".join(message))
    await ctx.channel.purge(limit=1)
#command18//shout
@client.command(aliases = ["me","say","shout"])
async def _shout(ctx, *shoutmessage):
    fullshoutmessage = " ".join(shoutmessage)
    await ctx.send(f":arrow_down:***HEY EVERYONE! <@!{str(ctx.author.id)}> SAYS:***\n\n***{str(fullshoutmessage)}***")
    await ctx.send(":arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:")
#command19//rps
@client.command(aliases = ["game","rps","rockpaperscissors"])
async def _rps(ctx, rpschoice):
    botrpschoice = random.choice(["Rock","Paper","Scissors"])
    if(rpschoice == botrpschoice.lower()):
        await ctx.send(f"***{botrpschoice}!***")
        await ctx.send("Ki! It's a draw!")
    elif(rpschoice == "rock" and botrpschoice == "Paper" or rpschoice == "paper" and botrpschoice == "Scissors" or rpschoice == "scissors" and botrpschoice == "Rock"):
        await ctx.send(f"***{botrpschoice}!***")
        await ctx.send("Wakay! I win!")
    elif(rpschoice == "rock" and botrpschoice == "Scissors" or rpschoice == "paper" and botrpschoice == "Rock" or rpschoice == "scissors" and botrpschoice == "Paper"):
        await ctx.send(f"***{botrpschoice}!***")
        await ctx.send("Oh no! I lost!")
    else:
        await ctx.send("**Invalid Request!**\nPlease input \"Rock\",\"Paper\", or\"Scissors\".")
#command20//link
@client.command(aliases = ["getlink","botlink","link","url","geturl","boturl","invitebot"])
async def _link(ctx):
    await ctx.send("***Bot Invite Link:\n***https://discord.com/api/oauth2/authorize?client_id=708053835704172574&permissions=10240&scope=bot ")

gettoken = open("token.txt","r")
token = gettoken.read()
client.run(token)
