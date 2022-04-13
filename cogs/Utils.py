import discord, datetime
import random
from discord.ext import commands
import asyncio

class Utils(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(description="Create a reminder!")
    async def remindme(self, ctx, mins:discord.Option(int, "Input how many minutes to remind"), reminder:discord.Option(str, "What you want to be reminded of.")):

        if not ctx.author:
            # print(ctx.author)
            await ctx.respond("You can't set reminder for other person.", ephemeral=True, delete_after=10)
            return

        if mins > 60:
            await ctx.respond("The limit for a reminder is 60 minutes.", ephemeral=True)
            return
        
        embed = discord.Embed(title="Reminder set", 
                description=f"{ctx.author.mention}, I have set a reminder for {reminder}",
                color=discord.Colour.dark_orange())
        await ctx.respond(embed=embed, delete_after=10)
        
        counter = 0
        while counter <= int(mins):
            counter += 1
            await asyncio.sleep(60)

            embed2 = discord.Embed(title="Reminder",
                    description=f"{ctx.author.mention}, your reminder for {reminder} with time of {mins} minutes has gone off.",
                    colour=discord.Colour.dark_orange())
            if counter == int(mins):
                await ctx.author.send(embed=embed2)
                break
    
    # , ctx, reminder:str, hour:int, minute:int, role:discord.Role, day:discord.Option(int, required=False)
    # @commands.slash_command(description="Schedule a event reminder.")
    # async def schedule(self, ctx):
        
        
    #     for member in ctx.guild.members:
    #         if member.roles == "Ociffer":
    #             print(member)
    #     now = datetime.datetime.now()
    #     if not day:
    #         then = now.replace(hour=hour, minute=minute)
    #         waitTime = (then-now).total_seconds()
    #         print(then)
    #     else:
    #         then = now.replace(day=day, hour=hour, minute=minute)
    #         print(then)
    #         waitTime = (then-now).total_seconds()
    #     print(waitTime)
    #     await asyncio.sleep(waitTime)
        


def setup(client):
    client.add_cog(Utils(client))