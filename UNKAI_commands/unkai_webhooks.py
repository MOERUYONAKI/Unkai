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

# - Commandes tests
''' async def wbk(ctx : commands.Context, nom : str, msg : str):
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

async def del_wbk(ctx : commands.Context, nom : str):
    wbk_list = await ctx.guild.webhooks()
    found = False

    for wbk in wbk_list:
        if nom.lower() == wbk.name.lower():
            await wbk.delete()
            await ctx.send(f"Le webhook \"{nom}\" a été supprimé")
            found = True

    if not found:
        await ctx.send(f"Webhook inconnu, suppression impossible") ''' 

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

async def check_message(message : discord.Message): 
    async with aiohttp.ClientSession() as session:
        WBK_list = WBK.get_webhooks_list(message.author.id) if WBK.get_webhooks_list(message.author.id) != False else []
        
        for i in range(len(WBK_list)):
            tag = f'{WBK_list[i][2]}/'
            if message.content[0 : len(tag)] == tag:
                # await message.channel.send(f'Tag détecté - **{tag[0 : -1]}**')

                if not WBK.is_register(WBK_list[i][0], message.guild.id):
                    await discord.StageChannel.create_webhook(self = message.channel, name = f'{WBK_list[i][1]}_{WBK_list[i][0]}')
                    WBK.set_registration(WBK_list[i][0], message.guild.id, message.guild.name)

                guild_WBK_list = await message.guild.webhooks()
                WBK_names = [elt.name for elt in guild_WBK_list]

                if f'{WBK_list[i][1]}_{WBK_list[i][0]}' in WBK_names:
                    webhook = Webhook.from_url(guild_WBK_list[WBK_names.index(f'{WBK_list[i][1]}_{WBK_list[i][0]}')].url, session = session)
                    await webhook.send(message.content[len(tag) :], username = WBK_list[i][1], avatar_url = WBK_list[i][3]) 


# base command

async def register(ctx : commands.Context, name : str, tag : str, avatar_url : str = None):
    if not check_validity(name) or not check_validity(tag):
        await ctx.send(f'Le nom et/ou le tag ne sont pas valide, opération impossible')

    else:
        avatar_url = 'https://cdn.discordapp.com/attachments/1206621721541484607/1206624037418303639/d130407ad3bb6a16a9a484ab626423b7.jpg' if avatar_url == None else avatar_url

        result = WBK.add_webhook(name, tag, ctx.author.id, ctx.author.name, avatar_url)

        if not result:
            await ctx.send(f'Une erreur est survenue, veuillez réessayer')

        else:
            await ctx.send(f'Le webhook "**{name}**" a bien été enregistré')

async def webhooks_list(ctx : commands.Context):
    WBK_list = WBK.get_webhooks_list(ctx.author.id)
    wbk_embed = discord.Embed(title = f'{ctx.author.name}\'s webhooks' , color = 0x00ffff)
    lines = 0

    for i in range(len(WBK_list)):
        wbk_embed.add_field(name = f'{i + 1} - {WBK_list[i][1]}', value = f'**Tag -** {WBK_list[i][2]} \n**Date de création -** {WBK_list[i][4]}', inline = False)
        lines += 1

    wbk_embed = discord.Embed(title = f'{ctx.author.name}\'s webhooks', description = 'Aucun webhook correspondant', color = 0x00ffff) if lines == 0 else wbk_embed

    await ctx.send(embed = wbk_embed)


# slash command

async def slash_register(interaction : discord.Interaction, name : str, tag : str, avatar_url : str = None): # Impossible de lier une image
    if not check_validity(name) or not check_validity(tag):
        await interaction.response.send_message(f'Le nom et/ou le tag ne sont pas valide, opération impossible')

    else:
        # avatar_url = 'https://cdn.discordapp.com/attachments/1206621721541484607/1206624037418303639/d130407ad3bb6a16a9a484ab626423b7.jpg' if avatar_url == None else avatar_url

        result = WBK.add_webhook(name, tag, interaction.user.id, interaction.user.name)

        if not result:
            await interaction.response.send_message(f'Une erreur est survenue, veuillez réessayer')

        else:
            await interaction.response.send_message(f'Le webhook "**{name}**" a bien été enregistré')

async def slash_webhooks_list(interaction : discord.Interaction):
    WBK_list = WBK.get_webhooks_list(interaction.user.id)
    wbk_embed = discord.Embed(title = f'{interaction.user.name}\'s webhooks' , color = 0x00ffff)
    lines = 0

    for i in range(len(WBK_list)):
        wbk_embed.add_field(name = f'{i + 1} - {WBK_list[i][1]}', value = f'**Tag -** {WBK_list[i][2]} \n**Date de création -** {WBK_list[i][4]}', inline = False)
        lines += 1

    wbk_embed = discord.Embed(title = f'{interaction.user.name}\'s webhooks', description = 'Aucun webhook correspondant', color = 0x00ffff) if lines == 0 else wbk_embed

    await interaction.response.send_message(embed = wbk_embed)