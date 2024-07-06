# ~ - - - - - - - - - - - - - - - - ~  U N K A I  ~ - - - - - - - - - - - - - - - - ~ #


# - - - - - - - - - - - - - - - -  I M P O R T S  - - - - - - - - - - - - - - - - #


from discord import *
import discord 
import asyncio
import numpy
import aiohttp
import os
from discord import FFmpegPCMAudio
from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord.ext.commands import has_permissions
from discord.shard import EventType
from discord.voice_client import VoiceClient
from discord import app_commands
from nacl import *
from time import sleep

# - UNKAI commands

import UNKAI_commands.unkai_help as unkai_help


# - - - - - - - - - - - - - - - -  A U T R E S  - - - - - - - - - - - - - - - - #


intents = discord.Intents.all()
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix = 'U!', description = 'narrateur rp', intents = intents)

embed = discord.Embed(title = "title", description = "description", color = 0x00ffff)
embed.add_field(name = "field", value = "value", inline = False)

bot.remove_command('help')


# - - - - - - - - - - - - - - - -  C L A S S E S  - - - - - - - - - - - - - - - - #





# - - - - - - - - - - - - - - - -  C O M M A N D E S  - - - - - - - - - - - - - - - - #


# PING - mesure du ping (fonctionnel)

@bot.command(name = 'ping')
async def ping(ctx : commands.Context): 
    print(round(bot.latency * 1000), "ms")
    await ctx.send(f'> *{round(bot.latency * 1000)} ms* \n> ||*...pong*||')

@bot.command(name = 'ms')
async def ms(ctx : commands.Context): 
    print(round(bot.latency * 1000), "ms")
    await ctx.send(f'> *{round(bot.latency * 1000)} ms*')

@bot.tree.command(name = 'ms')
async def slash_ms(interaction : discord.Interaction): 
    print(round(bot.latency * 1000), "ms")
    await interaction.response.send_message(f'> *{round(bot.latency * 1000)} ms*')


# HELP - aides : liste des commandes (fonctionnel)

@bot.command(name = 'help')
async def help(ctx : commands.Context, catégorie : str = 'all'):
    if catégorie.lower() == 'meteo':
        await unkai_help.help(ctx, 'meteo')

    elif catégorie.lower() == 'webhooks':
        await unkai_help.help(ctx, 'webhooks')

    else:
        await unkai_help.help(ctx)

@bot.tree.command(name = 'help')
@app_commands.choices(catégorie = [
    app_commands.Choice(name = 'Tout', value = 'all'),
    app_commands.Choice(name = "Météo", value = "meteo"),
    app_commands.Choice(name = "Webhooks", value = "webhooks")])
async def slash_help(interaction : discord.Interaction, catégorie : app_commands.Choice[str] = None): 
    await unkai_help.slash_help(interaction, catégorie.value if catégorie != None else 'all')


# - - - - - - - - - - - - - - - -  E V E N T S  - - - - - - - - - - - - - - - - #


@bot.event
async def on_ready():
    await bot.tree.sync()
    activity = discord.Game(name = "/help")
    await bot.change_presence(status = discord.Status.idle, activity = activity)

    print(f'Initialisation terminée ! \n{round(bot.latency * 1000)} ms')

@bot.event
async def on_message(message): # réaction aux messages (fonctionnel)
    await bot.process_commands(message)
    
    list_words = ['hey', 'heya', 'hello', 'yo', 'yop', 'coucou', 'cc', 'bonjour', 'bjr', 'bonsoir', 'bsr', 'salutation', 'salutations', 'salut', 'slt', 'salute', 're', 'wesh', 'wsh', 'salam']

    if message.content.lower() in list_words:
        await message.add_reaction("👋")
    
        if message.author.id == 489470853072027685:
            print(f'Moeru dit "{message.content.lower()}" !')
            await message.reply(f'{message.content} ô Moeru 👋')
        
        else:
            print(f'{message.author} dit "{message.content.lower()}"')

@bot.event
async def on_message_edit(before, after): # réaction aux messages (fonctionnel)
    list_words = ['hey', 'heya', 'hello', 'yo', 'yop', 'coucou', 'cc', 'bonjour', 'bjr', 'bonsoir', 'bsr', 'salutation', 'salutations', 'salut', 'slt', 'salute', 're', 'wesh', 'wsh', 'salam']
    Before = before.content.lower()
    After = after.content.lower()

    if Before in list_words and After in list_words:
        pass

    elif Before not in list_words and After in list_words:
        await after.add_reaction("👋")
    
        if after.author.id == 489470853072027685:
            await after.reply(f'{after.content} ô Moeru 👋')
    
    elif Before in list_words and After not in list_words:
        await after.remove_reaction(member = id('864220103113834516'), emoji = "👋")

    elif After == 'quoi':
        msg = await after.reply("feur")
        sleep(1.5)
        await msg.delete()

@bot.event     
async def on_member_join(member : discord.Member): # bienvenue (fonctionnel)
    print(f'{member} a rejoint un de nos serveurs ({member.guild})')

    try: # Message de bienvenue - mp
        await member.send("Bienvenue sur notre serveur !") 

    except: 
        pass

@bot.event
async def on_member_remove(member): # adieu (fonctionnel)
    print(f'{member} a quitté un de nos serveurs ({member.guild})')


# - - - - - - - - - - - - - - - -  T O K E N  - - - - - - - - - - - - - - - - #


bot.run("TOKEN")


# - - - - - - - - - - - - - - - -  I N F O R M A T I O N S  - - - - - - - - - - - - - - - - #

# > Actual version - 2 
# > Uid - 1
# > Creation - 2021/07 