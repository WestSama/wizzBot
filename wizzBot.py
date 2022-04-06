#wizzbot
import discord, os
from discord.ext import commands
from dotenv import load_dotenv
import random

#creds //get creds with os.getevn(TOKEN VARIABLE NAME)
load_dotenv()

intents = discord.Intents.all()
intents.members = True
intents.message_content = True

activity = discord.Game(name="Lost Ark EU")

bot = discord.Bot(intents=discord.Intents.all(), activity=activity)

@bot.event
async def on_ready():
    print(f'{bot.user} is ready and Online!')

@bot.event
async def on_message(message):

    msgs = ["Don't ping me you blob!",
            "I will kill you if you ping me!",
            "I dare you to ping me again!",
            "Who pinged me! REEEE",
            "Poke, poke, poke is that all you do?"
    ]
    msgBot = random.choice(msgs)
    if message.content.startswith("<@760636930265317450>"):
        await message.channel.send(msgBot)

@bot.event
async def on_member_remove(member:discord.User):
    channel = bot.get_channel(520931518655234048)
    await channel.send(f"{member} -- {member.display_name} has left the server!")

@bot.command(description="Is this user sus??")
async def sus(ctx, member: discord.Member):
    susMsg = [
            f"{member.name} is sus!",
            f"{member.name} isn't sus."
    ]
    susSend = random.choice(susMsg)
    await ctx.respond(susSend)

@bot.command(description="Bot will greet you with a msg.")
async def hello(ctx):
    helloMsgs = [f"{ctx.author.mention} hello you blob!",
                f"{ctx.author.mention} hello only to you wizzel.",
                f"{ctx.author.mention} no hello for you today."
    ]
    msg = random.choice(helloMsgs)
    await ctx.respond(msg)


@bot.command(description="Use this command to slap a user.")
async def slap(ctx, member: discord.Member):
    
    await ctx.respond(f"{ctx.author.name} slapped {member.mention}!!!")

bot.run(os.getenv('WIZZBOT_TOKEN'))
