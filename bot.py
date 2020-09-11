import discord
import os
import datetime
from discord.ext import commands, tasks
from itertools import cycle
from termcolor import cprint

bot = commands.Bot(command_prefix='.')
status = cycle(['A', 'B', 'C'])

file = open(".token")
token = file.read().replace("\n", "")
file.close()

@bot.event
async def on_ready():
    change_status.start()
    print(f'[{datetime.datetime.now(tz=datetime.timezone.utc)}]')
    cprint('Bot is online.', 'green')


@tasks.loop(seconds=1)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))


@bot.command(hidden=True)
async def ld(ctx, extension):
    bot.load_extension(f'cogs.{extension}')


@bot.command(hidden=True)
async def uld(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')


@bot.command(hidden=True)
async def rld(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(str(token))
