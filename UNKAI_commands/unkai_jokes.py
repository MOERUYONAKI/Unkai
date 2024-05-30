from discord import *
import discord 
from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord.ext.commands import has_permissions
from discord.shard import EventType
from discord import app_commands
from nacl import *
from time import *
from random import choice

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix = 'U!', description = 'narrateur rp', intents = intents)

jokes = { # - Nombre de "blagues" : 10
    'Quel animal a trois bosses ?' : 'Un chameau qui s’est cogné',
    'Qu’est-ce qu’une manifestation d’aveugles ?' : 'Le festival de Cannes',
    'Que dit une orange à une pomme ?' : 'Rien, les fruits ne parlent pas',
    'Pourquoi les sorcières volent sur des balais ?' : 'Parce que les aspirateurs font trop de bruit',
    'Quel est le pays le plus cool du monde ?' : 'Le Yémen. Yeah man',
    'Qu\'est ce qui a 13 cœurs mais aucun autre organe ?' : 'Un jeu de cartes',
    'Que prend un éléphant dans un bar ?' : 'Beaucoup de place',
    'Qu\'est ce qui a 118 yeux et 7 dents ?' : 'Un autobus rempli de personnes âgées',
    'Comment on appelle un avion qui rebondit ?' : 'Un Boing',
    'Quel est l\'animal qui a le plus de dents ?' : 'La petite souris'
}


# base command

async def joke(ctx : commands.Context):
    joke = choice(list(jokes.keys()))

    await ctx.send(f'***{joke}***\n> ||{jokes[joke]}||')
    print('blague délivré avec succès !')


# slash command

async def slash_joke(interaction : discord.Interaction):
    joke = choice(list(jokes.keys()))

    await interaction.response.send_message(f'***{joke}***\n> ||{jokes[joke]}||')
    print('blague délivré avec succès !')