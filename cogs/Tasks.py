import discord, os, datetime
from discord.ext import commands, tasks
import random

tz = datetime.timezone(datetime.timedelta(hours=1))
when = [
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
        datetime.time(12, 55, tzinfo=tz),
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
]
morningTime = [datetime.time(8, 0, tzinfo=tz)]

class Tasks(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.autoPurge.start()
        self.goodMorning.start()

    @tasks.loop(time=when)
    async def autoPurge(self):
        print("I have started the purge.")
        channel = self.client.get_channel(839277245516480533)
        await channel.purge()

    @tasks.loop(time=morningTime)
    async def goodMorning(self):
        channel = self.client.get_channel(837066959757377597)
        await channel.send(f"Good morning you beautiful people <:pepouwu:741440883760693349>")


def setup(client):
    client.add_cog(Tasks(client))