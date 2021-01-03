import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print("Bot connected!")
    print (f"{bot.user.name}#{bot.user.discriminator}")
bot.run('Nzk0NjcxNDkyNzk2MjUyMjAy.X--NgA.0RaKShPBKpOMTodjSFHIjtb6Ti8')
