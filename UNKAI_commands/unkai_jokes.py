from discord import *
import discord 
from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord.ext.commands import has_permissions
from discord.shard import EventType
from discord import app_commands
from nacl import *
from time import *
from random import randint

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix = 'U!', description = 'narrateur rp', intents = intents)


# base command

async def joke(ctx):
    joke_id = randint(1,7)

    if joke_id == 1:
        await ctx.send(f'***Quel animal a trois bosses ?***\n> ||Un chameau qui s’est cogné||')

    elif joke_id == 2:
        await ctx.send(f'***Qu’est-ce qu’une manifestation d’aveugles ?***\n> ||Le festival de Cannes||')

    elif joke_id == 3:
        await ctx.send(f'***Que dit une orange à une pomme ?***\n> ||Rien, les fruits ne parlent pas||')

    elif joke_id == 4:
        await ctx.send(f'***Pourquoi les sorcières volent sur des balais ?***\n> ||Parce que les aspirateurs font trop de bruit||')

    elif joke_id == 5:
        await ctx.send(f'***Quel est le pays le plus cool du monde ?***\n> ||Le Yémen. Yeah man||')

    elif joke_id == 6:
        await ctx.send(f"***Qu'est ce qui a 13 cœurs mais aucun autre organe ?***\n> ||Un jeu de cartes||")

    elif joke_id == 7:
        await ctx.send(f'***Que prend un éléphant dans un bar ?***\n> ||Beaucoup de place||')

    print('blague délivré avec succès !')


# slash command

async def slash_joke(interaction : discord.Interaction):
    joke_id = randint(1,7)

    if joke_id == 1:
        await interaction.response.send_message(f'***Quel animal a trois bosses ?***\n> ||Un chameau qui s’est cogné||')

    elif joke_id == 2:
        await interaction.response.send_message(f'***Qu’est-ce qu’une manifestation d’aveugles ?***\n> ||Le festival de Cannes||')

    elif joke_id == 3:
        await interaction.response.send_message(f'***Que dit une orange à une pomme ?***\n> ||Rien, les fruits ne parlent pas||')

    elif joke_id == 4:
        await interaction.response.send_message(f'***Pourquoi les sorcières volent sur des balais ?***\n> ||Parce que les aspirateurs font trop de bruit||')

    elif joke_id == 5:
        await interaction.response.send_message(f'***Quel est le pays le plus cool du monde ?***\n> ||Le Yémen. Yeah man||')

    elif joke_id == 6:
        await interaction.response.send_message(f"***Qu'est ce qui a 13 cœurs mais aucun autre organe ?***\n> ||Un jeu de cartes||")

    elif joke_id == 7:
        await interaction.response.send_message(f'***Que prend un éléphant dans un bar ?***\n> ||Beaucoup de place||')

    print('blague délivré avec succès !')