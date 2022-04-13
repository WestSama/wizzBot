import discord, os, datetime
from discord.ext import commands, tasks
import random


roleIDs = {"Group 1":842539135473942539,
            "Group 2":842554862109196308,
            "Group 3":842523768483741717,
            "Group 4":842554987174690866}

class roleView(discord.ui.View):
    @discord.ui.select(placeholder="Choose your role...",
                        min_values=1,
                        max_values=1,
                        options = [
                            discord.SelectOption(
                                label="Group 1",
                                description="Choose this role if you are in Group 1",
                            ),
                            discord.SelectOption(
                                label="Group 2",
                                description="Choose this role if you are in Group 2"
                            ),
                            discord.SelectOption(
                                label="Group 3",
                                description="Choose this role if you are in Group 3"
                            ),
                            discord.SelectOption(
                                label="Group 4",
                                description="Choose this role if you are in Group 4"
                            ),
                        ])
    async def selectCallback(self, select, interaction):
        user = interaction.user
        guild = interaction.guild
        
        for role in roleIDs:
            if select.values[0] == role:
                role = guild.get_role(roleIDs[role])
                if role not in user.roles:
                    await user.add_roles(role)
                    await interaction.response.send_message("Role has been added.", ephemeral=True, delete_after= 10)
                else:
                    await user.remove_roles(role)
                    await interaction.response.send_message("Role has been removed.", ephemeral=True, delete_after= 10)

class Roles(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.slash_command(description="Command to select roles in the server.")
    async def role(self, ctx):
        await ctx.respond(view=roleView(), ephemeral=True, delete_after= 30)

def setup(client):
    client.add_cog(Roles(client))