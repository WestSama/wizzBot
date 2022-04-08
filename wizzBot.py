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

<<<<<<< HEAD
bot = commands.Bot(debug_guilds=[763654705649156098, 514264673831616512], intents=discord.Intents.all(), activity=activity, command_prefix="!")
=======
bot = discord.Bot(intents=discord.Intents.all(), activity=activity)
>>>>>>> e907b77329de31ef2ec548602172e79dd6ab91a3

@bot.event
async def on_ready():
    print(f'{bot.user} is ready and Online!')

for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")

<<<<<<< HEAD
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")
    await ctx.send("Loaded cog!")

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")
    await ctx.send("Unloaded cog!")
=======
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
>>>>>>> e907b77329de31ef2ec548602172e79dd6ab91a3

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f"cogs.{extension}")
    await ctx.send("Reloaded cog!")

bot.run(os.getenv('WIZZBOT_TOKEN'))
