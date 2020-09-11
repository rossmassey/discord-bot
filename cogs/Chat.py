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
                cprint(
                    f'{log.user(message)} attached {attachment.filename} ({attachment.size/1000000} mb)', 'magenta')

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        cprint(f'{log.user(after)}[e]: {after.content}')

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        cprint(f'{log.user(message)} deleted {message.content}', 'red')

def setup(bot):
    bot.add_cog(Chat(bot))
