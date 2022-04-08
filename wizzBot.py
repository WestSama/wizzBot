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


bot = commands.Bot(debug_guilds=[763654705649156098, 514264673831616512], intents=discord.Intents.all(), activity=activity)

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

bot.run(os.getenv('WIZZBOT_TOKEN'))
