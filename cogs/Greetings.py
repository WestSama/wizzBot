import discord
import random
from discord.ext import commands


class Greetings(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        # print(message.content)
        msgs = ["Don't ping me you blob!",
                "I will kill you if you ping me!",
                "I dare you to ping me again!",
                "Who pinged me! REEEE",
                "Poke, poke, poke is that all you do?"
        ]
        msgBot = random.choice(msgs)
        if message.content.startswith("<@760636930265317450>"):
            await message.channel.send(msgBot)
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.client.get_channel(520931518655234048)
        await channel.send(f"{member} -- {member.display_name} has join the server!")


    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.client.get_channel(520931518655234048)
        await channel.send(f"{member} -- {member.display_name} has left the server!")

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        channel = self.client.get_channel(520931518655234048)
        if before.nick != after.nick:

            await channel.send(f"{before.name} changed his/her name to {after.nick}")

    @commands.slash_command(description="Is this user sus??")
    async def sus(self, ctx, member: discord.Member):
        susMsg = [
                f"{member.name} is sus!",
                f"{member.name} isn't sus."
        ]
        susSend = random.choice(susMsg)
        await ctx.respond(susSend)

    @commands.slash_command(description="Bot will greet you with a msg.")
    async def hello(self, ctx):
        helloMsgs = [f"{ctx.author.mention} hello you blob!",
                    f"{ctx.author.mention} hello only to you wizzel.",
                    f"{ctx.author.mention} no hello for you today."
        ]
        msg = random.choice(helloMsgs)
        await ctx.respond(msg)


    @commands.slash_command(description="Use this command to slap a user.")
    async def slap(self, ctx, member: discord.Member):
        print(member)
        await ctx.respond(f"{ctx.author.name} slapped {member.mention}!!!")

def setup(client):
    client.add_cog(Greetings(client))