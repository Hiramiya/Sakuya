from discord import TextChannel
from discord.ext import commands
from discord.ext.commands import Bot


class Settings(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.group()
    async def enable(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Enable what?')

    @enable.command(name='sentinel')
    @commands.has_guild_permissions(ban_members=True)
    async def enable_sentinel(self, ctx, *, alert_channel: TextChannel = None):
        await self.bot.get_cog('Sentinel').enable(ctx, alert_channel)

    @enable.command(name='mewo')
    @commands.has_guild_permissions(manage_guild=True)
    async def enable_mewo(self, ctx):
        await self.bot.get_cog('Mewo').enable(ctx)

    @commands.group()
    async def disable(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Disable what? You?')

    @disable.command(name='sentinel')
    @commands.has_guild_permissions(ban_members=True)
    async def disable_sentinel(self, ctx):
        await self.bot.get_cog('Sentinel').disable(ctx)

    @disable.command(name='mewo')
    @commands.has_guild_permissions(manage_guild=True)
    async def disable_mewo(self, ctx):
        await self.bot.get_cog('Mewo').disable(ctx)


def setup(bot):
    bot.add_cog(Settings(bot))
