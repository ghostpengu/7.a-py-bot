import ctypes
from http import client
import os
import string
import random

import discord
from discord.ext import commands
tokenforbot = input(string)
bot = commands.Bot(command_prefix='.', description="This is a Helper Bot")



@bot.command()
async def pleska(ctx):
    await ctx.send('alexova')
    

@bot.command()
async def ask(ctx,*,Question):
    responses = ["Ano",
                "Nie",
                "Mozno",
                "Urcite",
                "Si Gay",
                "Ok",
                "Idk",
                "Neviem",
                "alex",
                "Ano a mas maly pp btw",
                "ti jebe",
                "NN",
                "Jj",
                "Ti Mrda?"]
 
    await ctx.send(f'Otazka: {Question} Odpoved: {random.choice(responses)}')

@bot.command()
async def ping(ctx):
    embed=discord.Embed()
    embed.add_field(name="Ping", value="Pong", inline=False)
    await ctx.send(embed=embed)
    
bot.run(tokenforbot)