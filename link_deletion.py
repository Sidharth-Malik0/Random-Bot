import discord
from discord.ext import commands

class LinkDeletion(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if "http://" in message.content or "https://" in message.content:
            await message.delete()
            await message.channel.send(f"{message.author.mention}, please don't post links in this server.")