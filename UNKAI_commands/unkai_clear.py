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

async def clear(ctx : commands.Context, nombre : int = 1) : # suppression de messages (fonctionnel)
    print('Suppression en cours')
    adv = ''

    if nombre <= 0:
        nombre = 1

    elif nombre > 5:
        adv = '> *En raison des préventions contre le spam de Discord, la commande \"**U!clear**\" est désormais limitée à **5** messages...*'
        nombre = 5
        
    msgs = -1
    async for message in ctx.channel.history(limit = nombre + 1):
        msgs += 1
        await message.delete()
    
    if msgs == 0 or msgs == 1:
        print(msgs,'message supprimé')
        msg = await ctx.send(f'{msgs} message supprimé \n \n{adv}')
        sleep(2)
        await msg.delete()
    
    else:
        print(msgs, 'messages supprimés')
        msg = await ctx.send(f'{msgs} messages supprimés \n \n{adv}')
        sleep(2)
        await msg.delete()


# slash command

async def slash_clear(interaction : discord.Interaction, nombre : int = 1) : # suppression de messages (fonctionnel)
    print('Suppression en cours')
    adv = ''

    if nombre <= 0:
        nombre = 1

    elif nombre > 5:
        adv = '> *En raison des préventions contre le spam de Discord, la commande \"**U!clear**\" est désormais limitée à **5** messages...*'
        nombre = 5
        
    msgs = 0
    async for message in interaction.channel.history(limit = nombre):
        msgs += 1
        await message.delete()
    
    if msgs == 0 or msgs == 1:
        print(msgs,'message supprimé')
        await interaction.response.send_message(f'{msgs} message supprimé \n \n{adv}', ephemeral = True, delete_after = 2)
    
    else:
        print(msgs, 'messages supprimés')
        await interaction.response.send_message(f'{msgs} messages supprimés \n \n{adv}', ephemeral = True, delete_after = 2)