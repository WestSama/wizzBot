import discord
import random
from discord.ext import commands
import asyncio


class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(description="Deletes messages in the current channel.")
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, limit: discord.Option(int, "Input the number of messages to delete.")): 
        await ctx.channel.purge(limit=limit)
        await ctx.respond(f"I have deleted {limit} messages.", delete_after=10)

    @purge.error
    async def purgeError(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permissions.", ephemeral=True)

def setup(client):
    client.add_cog(Moderation(client))