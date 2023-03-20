import discord

async def send_welcome_message(member):
    channel = discord.utils.get(member.guild.channels, name='general')
    welcome_message = f"Welcome to the server, {member.mention}! Please introduce yourself in the introductions channel."
    await channel.send(welcome_message)