import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """Kicks the specified member from the server."""
        await member.kick(reason=reason)
        await ctx.send(f"{member} has been kicked.")

    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """Bans the specified member from the server."""
        await member.ban(reason=reason)
        await ctx.send(f"{member} has been banned.")

    @commands.command()
    async def purge(self, ctx, limit=10):
        """Deletes the last <limit> messages in the current channel."""
        await ctx.channel.purge(limit=limit+1)
        await ctx.send(f"{limit} messages have been deleted.", delete_after=5)

    @commands.command()
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        """Mutes the specified member in the server."""
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not role:
            role = await ctx.guild.create_role(name="Muted", reason="Mute command")
            for channel in ctx.guild.channels:
                await channel.set_permissions(role, send_messages=False)
        await member.add_roles(role, reason=reason)
        await ctx.send(f"{member} has been muted.")

    @commands.command()
    async def unmute(self, ctx, member: discord.Member, *, reason=None):
        """Unmutes the specified member in the server."""
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        if role in member.roles:
            await member.remove_roles(role, reason=reason)
            await ctx.send(f"{member} has been unmuted.")
        else:
            await ctx.send(f"{member} is not muted.")