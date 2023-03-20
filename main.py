import discord
from discord.ext import commands
from welcome import send_welcome_message
from moderation import Moderation
from link_deletion import LinkDeletion

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_member_join(member):
    await send_welcome_message(member)

bot.add_cog(Moderation(bot))
bot.add_cog(LinkDeletion(bot))

bot.run("Token")
