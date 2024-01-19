from discord import *
import discord 
from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord.ext.commands import has_permissions
from discord.shard import EventType
from discord import app_commands
from nacl import *
import aiohttp

async def wbk(ctx : commands.Context, nom : str, * , msg : str):
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