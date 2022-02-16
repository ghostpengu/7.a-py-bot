import os
import string

import discord
from discord.ext import commands
tokenforbot = input(string)
bot = commands.Bot(command_prefix='.', description="This is a Helper Bot")



@bot.command()
async def pleska(ctx):
    await ctx.send('alexova')
    

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
bot.run(tokenforbot)