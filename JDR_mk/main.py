# - - - - - - - - - - -  I M P O R T S  - - - - - - - - - - - #

from discord import *
import discord 
from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord.ext.commands import has_permissions
from discord.shard import EventType
from discord import app_commands
from nacl import *
from .chapters import *
from .inventory import *
from .mk_db import *


# - - - - - - - - - - -  S C R I P T  - - - - - - - - - - - #

# - Génération de l'inventaire
def inventory_init(username : str, userid : int): 
    inventaire = Inventaire()
    player = Players()
    item_list = get_item_list()

    player.add_user(username, userid)

    for item_name in item_list:
        if player.is_in_inventory(userid, item_name):
            inventaire.inventory[item_name] = player.get_quantity(userid, item_name)

    return inventaire

# - Lancement de l'aventure
async def jdr_start(ctx : commands.Context):
    inventaire = inventory_init(ctx.message.author.name, ctx.message.author.id)

    character = Character(ctx.message.author.name, inventaire)
    # presentation(inventaire, character)