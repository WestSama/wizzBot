@bot.slash_command(name="hello", description = "Say hello to the bot")
async def hellow(ctx):
    await ctx.send("Hey!")

"""How to setup an embed"""
@bot.command(description="Sends an Embed!")
async def create_embed(ctx):
    embed = discord.Embed(
        title="My Embed",
        description="Pycord makes embeds easy to use and create!",
        color=discord.Colour.blue(),
    )

    embed.add_field(name="Test field", value="This is a test field")
    embed.add_field(name="Inline Fields?", value="Of course we support inline fields!", inline=True)
 
    embed.set_footer(text="This is an embed generated with Pycord.")
    embed.set_author(name="Pycord Embed", icon_url="https://avatars.githubusercontent.com/u/89700626")
    embed.set_thumbnail(url="https://avatars.githubusercontent.com/u/89700626")
    embed.set_image(url="https://i.imgur.com/6Yj6pBe.png")
    await ctx.respond(embed=embed)

"""How to setup a dropdown"""
class MyView(discord.ui.View):

    @discord.ui.select(
        placeholder = "Choose a Flavor!",
        min_values = 1,
        max_values = 1,
        options = [
            discord.SelectOption(
                label="Vanilla",
                description="Pick this if you like vanilla!"
            ),
            discord.SelectOption(
                label="Chocolate",
                description="Pick this if you like chocolate!"
            ),
            discord.SelectOption(
                label="Strawberry",
                description="Pick this if you like strawberry!"
            )
        ]
    )
    
    async def callback(self, select, interaction: discord.Interaction):
        if select.values[0] == "Vanilla":
            
            await interaction.response.send_message(f"Awesome! I like {select.values[0]} too!")

"""Command to call dropdown"""
@bot.command(description="Creates a dropdown")
async def dropdown(ctx):
    view = MyView()
    embed = discord.Embed(
        title="Hello There!",
        description=None,
        color=discord.Color.random()
    )
    await ctx.respond(embed=embed, view=view)

"""More testing
Context Menus"""

@bot.user_command(name="Is User Sus", guild_ids=[763654705649156098])
async def is_this_user_sus(ctx, member: discord.Member):
    await ctx.respond(f"{member.name} is {'not sus' if member.id == 543397958197182464 else 'sus'}")

@bot.message_command(name="Is Message Sus")  # creates a global message command. use guild_ids=[] to create guild-specific commands.
async def is_this_msg_sus(ctx, message: discord.Message):  # message commands return the message
    await ctx.respond(f"Message {message.id} sent by {message.author} is {'not sus' if message.id == 543397958197182464 else 'sus'}")

"""Buttons test"""
class View(discord.ui.View): # Create a class called View that subclasses discord.ui.View
    @discord.ui.button(label="Click me!", style=discord.ButtonStyle.primary, emoji="😎") # Create a button with the label "😎 Click me!" with color Blurple
    async def button_callback(self, button, interaction):
        await interaction.response.send_message("You clicked the button!") # Send a message when the button is clicked

@bot.slash_command() # Create a slash command
async def button(ctx):
    await ctx.respond("This is a button!", view=View()) # Send a message with our View class that contains the button


"""Threads"""
@bot.slash_command()
async def createthread(ctx):
    # message = await ctx.send("My Starting Message")
    # await message.create_thread(name="thread name", auto_archive_duration=60)
    
    """To create thread in specific channel it required Guild Level higher"""
    channel = bot.get_channel(763654706144739330) # define this!
    await channel.create_thread(name="Thread Name", message=None, auto_archive_duration=60, type=None, reason=None)



    datetime.time(0, 55, tzinfo=tz),
        datetime.time(1, 55, tzinfo=tz),
        datetime.time(2, 55, tzinfo=tz),
        datetime.time(3, 55, tzinfo=tz),
        datetime.time(4, 55, tzinfo=tz),
        datetime.time(5, 55, tzinfo=tz),
        datetime.time(6, 55, tzinfo=tz),
        datetime.time(7, 55, tzinfo=tz),
        datetime.time(8, 55, tzinfo=tz),
        datetime.time(9, 55, tzinfo=tz),
        datetime.time(10, 55, tzinfo=tz),
        datetime.time(11, 55, tzinfo=tz),
        datetime.time(12, 9, tzinfo=tz),
        datetime.time(13, 55, tzinfo=tz),
        datetime.time(14, 55, tzinfo=tz),
        datetime.time(15, 55, tzinfo=tz),
        datetime.time(16, 55, tzinfo=tz),
        datetime.time(17, 55, tzinfo=tz),
        datetime.time(18, 55, tzinfo=tz),
        datetime.time(19, 55, tzinfo=tz),
        datetime.time(20, 55, tzinfo=tz),
        datetime.time(21, 55, tzinfo=tz),
        datetime.time(22, 55, tzinfo=tz),
        datetime.time(23, 55, tzinfo=tz),