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
        if len(message.attachments) > 0:
            for attachment in message.attachments:
                print(
                    f'{log.user(message)} attached {attachment.filename} ({attachment.size/1000000} mb)')


def setup(bot):
    bot.add_cog(Chat(bot))
