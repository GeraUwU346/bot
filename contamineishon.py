import discord
import os
import random
import asyncio
from discord.ext import commands

frases = ["recuerda separar la basura organica de la inorganica"
                  ,"¿Sabias que se puede hacer composta mezclando hojas secas con tierra?"
                  ,"no quemes basura!"
                  ,"riega las plantas en la noche!"
                  ,"reutiliza los envases de botellas y/o latas"]
        

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
    
@bot.command()
async def gay(ctx):
    await ctx.send(f'el que se oponga es gay  {bot.user}!')
    
async def enviar_mensaje():
    random.choice[frases]
    print
        





bot.run("Token")