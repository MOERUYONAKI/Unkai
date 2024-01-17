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


# base command

async def clear(ctx, nombre : int = 1) : # suppression de messages (fonctionnel)
    print('Suppression en cours')
    if nombre <= 0:
        nombre = 1
        
    msgs = -1
    async for message in ctx.channel.history(limit = nombre + 1):
        msgs += 1
        await message.delete()
    
    if msgs == 0 or msgs == 1:
        print(msgs,'message supprimé')
        msg = await ctx.send(f'{msgs} message supprimé')
        sleep(1.5)
        await msg.delete()
    
    else:
        print(msgs, 'messages supprimés')
        msg = await ctx.send(f'{msgs} messages supprimés')
        sleep(1.5)
        await msg.delete()


# slash command

async def slash_clear(interaction : discord.Interaction, nombre : int = 1) : # suppression de messages (fonctionnel)
    print('Suppression en cours')
    if nombre <= 0:
        nombre = 1
        
    msgs = 0
    async for message in interaction.channel.history(limit = nombre):
        msgs += 1
        await message.delete()
    
    if msgs == 0 or msgs == 1:
        print(msgs,'message supprimé')
        msg = await interaction.response.send_message(f'{msgs} message supprimé')
        sleep(1.5)
        await interaction.delete_original_response()
    
    else:
        print(msgs, 'messages supprimés')
        msg = await interaction.response.send_message(f'{msgs} messages supprimés')
        sleep(1.5)
        await interaction.delete_original_response()