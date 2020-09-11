import discord
from discord.ext import commands
from termcolor import cprint

import log


class Chat(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        print(
            f'{log.user(message)}: {message.content}')


def setup(bot):
    bot.add_cog(Chat(bot))
