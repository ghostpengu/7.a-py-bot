import os

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='.', description="This is a Helper Bot")





@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
bot.run('OTQzNTEzODE2OTYzMTA0ODI4.Yg0Jtw.FNW3eYPHxQ3ZqDkrvUvaPEnI--o')