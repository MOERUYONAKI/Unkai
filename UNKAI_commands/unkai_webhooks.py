from discord import *
import discord 
from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord.ext.commands import has_permissions
from discord.shard import EventType
from discord import app_commands
from nacl import *
import aiohttp
from .DataBases.UNKAI_wbk.UNKAI_wbk_DB import Webhooks


''' 
async def wbk(ctx : commands.Context, nom : str, msg : str):
    async with aiohttp.ClientSession() as session:
        wbk_list = await ctx.guild.webhooks()
        found = False

        for wbk in wbk_list:
            if nom.lower() == wbk.name.lower():
                webhook = Webhook.from_url(wbk.url, session = session)
                await webhook.send(msg, avatar_url = "https://cdn.discordapp.com/attachments/1155450092329906238/1197196427508588575/9da2bf5e-1630-4586-a1e0-8422eb51c3e8.png?ex=65ba630f&is=65a7ee0f&hm=9a8f24db2fbe28cb3ed6897fcb897eeaf5ab5bee3e6663dfb3f96f2883a71c3b&")
                found = True

        if not found:
            await ctx.send(f"Webhook inconnu, essayez \"U!wbk_create\"")

async def create_wbk(ctx : commands.Context, nom : str):
    wbk_list = await ctx.guild.webhooks()
    found = False

    for wbk in wbk_list:
        if nom.lower() == wbk.name.lower():
            await ctx.send(f"Le webhook \"{nom}\" est déjà présent sur ce serveur")
            found = True

    if not found:
        await discord.StageChannel.create_webhook(self = ctx.channel, name = nom)
        await ctx.send(f"Un webhook du nom de \"{nom}\" a été créé")

async def del_wbk(ctx : commands.Context, nom : str):
    wbk_list = await ctx.guild.webhooks()
    found = False

    for wbk in wbk_list:
        if nom.lower() == wbk.name.lower():
            await wbk.delete()
            await ctx.send(f"Le webhook \"{nom}\" a été supprimé")
            found = True

    if not found:
        await ctx.send(f"Webhook inconnu, suppression impossible")
''' # Commandes tests

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix = 'U!', description = 'narrateur rp', intents = intents)
WBK = Webhooks()

def check_validity(string : str): # True si valide, False sinon 
    word = ""

    string = string.split()
    for i in range(len(string)):
        word += string[i]

    string = word.split("/")
    for i in range(len(string)):
        word += string[i]

    string = word.split("\\")
    for i in range(len(string)):
        word += string[i]

    return True if word != [] else False


# base command

async def register(ctx : commands.Context, name : str, tag : str, avatar_url : str = None):
    if not check_validity(name) or not check_validity(tag):
        await ctx.send(f'Le nom et/ou le tag ne sont pas valide, opération impossible')

    else:
        result = WBK.add_webhook(name, tag, ctx.author.id, ctx.author.name, avatar_url)

        if not result:
            await ctx.send(f'Une erreur est survenue, veuillez réessayer')
            return False

        await ctx.send(f'Le webhook "{name}" a bien été enregistré')


# slash command

