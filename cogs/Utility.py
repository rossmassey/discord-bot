import discord
from discord.ext import commands
from termcolor import cprint

import log


class Utility(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief='shows your ping')
    async def ping(self, ctx):
        ping = round(self.bot.latency * 1000)
        cprint(
            (f'{log.user(ctx.message)} pinged with {ping} ms'), 'blue')
        await ctx.send(f'`Response: {ping} ms`')

    @commands.command(brief='clears [x] lines')
    async def clear(self, ctx, amount=1):
        await ctx.channel.purge(limit=(amount + 1))
        cprint(
            (f'{log.user(ctx.message)} cleared {amount} lines'), 'blue')


def setup(bot):
    bot.add_cog(Utility(bot))
