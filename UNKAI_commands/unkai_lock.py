from discord import *
import discord 
from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord.ext.commands import has_permissions
from discord.shard import EventType
from discord import app_commands
from nacl import *
from time import *

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix = 'U!', description = 'narrateur rp', intents = intents)


# base commands

async def lock(ctx : commands.Context, serveurs : list):
    for serveur in serveurs:
        if serveur.id == ctx.guild.id:

            if serveur.check_status():
                lock = serveur.status_lock()
                await ctx.send(f'> Serveur verrouillé')
                print(lock, f'({ctx.guild.name})')

            else:
                await ctx.send(f'Ce serveur est déjà verrouillé')

async def unlock(ctx : commands.Context, serveurs : list):
    for serveur in serveurs:
        if serveur.id == ctx.guild.id:

            if not serveur.check_status():
                lock = serveur.status_unlock()
                await ctx.send(f'> Serveur déverrouillé')
                print(lock, f'({ctx.guild.name})')

            else:
                await ctx.send(f"Ce serveur n'est pas verrouillé")


# slash commands

async def slash_lock(interaction : discord.Interaction, serveurs : list):
    for serveur in serveurs:
        if serveur.id == interaction.guild.id:

            if serveur.check_status():
                lock = serveur.status_lock()
                await interaction.response.send_message(f'> Serveur verrouillé')
                print(lock, f'({interaction.guild.name})')

            else:
                await interaction.response.send_message(f'Ce serveur est déjà verrouillé')

async def slash_unlock(interaction : discord.Interaction, serveurs : list):
    for serveur in serveurs:
        if serveur.id == interaction.guild.id:

            if not serveur.check_status():
                lock = serveur.status_unlock()
                await interaction.response.send_message(f'> Serveur déverrouillé')
                print(lock, f'({interaction.guild.name})')

            else:
                await interaction.response.send_message(f"Ce serveur n'est pas verrouillé")