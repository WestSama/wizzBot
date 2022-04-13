#wizzbot

import discord, os, datetime, asyncio
from discord.ext import commands, tasks
from dotenv import load_dotenv
import random

#creds //get creds with os.getevn(TOKEN VARIABLE NAME)
load_dotenv()

intents = discord.Intents.all()
intents.members = True
intents.message_content = True
intents.guilds = True

activity = discord.Game(name="Lost Ark EU")

bot = commands.Bot(debug_guilds=[763654705649156098, 514264673831616512], intents=discord.Intents.all(), activity=activity, command_prefix="!")

@bot.event
async def on_ready():
    print(f'{bot.user} is ready and Online!')
      

for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")
    await ctx.send("Loaded cog!")

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")
    await ctx.send("Unloaded cog!")

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f"cogs.{extension}")
    await ctx.send("Reloaded cog!")

@bot.slash_command()
async def testmember(ctx, role: discord.Role):
    members = role.members
    for member in members:
        print(f"{member.display_name} -- {member.id}")
        await member.send("Hello")
        await asyncio.sleep(1)
bot.run(os.getenv('WIZZBOT_TOKEN'))
