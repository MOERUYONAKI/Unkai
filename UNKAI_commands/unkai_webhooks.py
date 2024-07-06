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

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix = 'U!', description = 'narrateur rp', intents = intents)
WBK = Webhooks()

class button_view(discord.ui.View): # Changement de page (wbk_list)
    def __init__(self, Uid : int):
        super().__init__(timeout = None)
        self.Uid = Uid
        self.page_id = 1
        self.max_page = 0
        
    @discord.ui.button(label = "⬅️", custom_id = "left")
    async def left(self, interaction : discord.Interaction, button : discord.ui.Button):
        if interaction.user.id == self.Uid:
            WBK_list = WBK.get_webhooks_list(interaction.user.id) if WBK.get_webhooks_list(interaction.user.id) else []
            self.max_page = len(WBK_list)
            lines = 0

            if self.page_id > 1:
                self.page_id -= 1

            wbk_embed = discord.Embed(title = f'{interaction.user.name}\'s webhooks - page {self.page_id}' , color = 0x00ffff)

            for i in range((10 * (self.page_id - 1)), len(WBK_list)):
                wbk_embed.add_field(name = f'{i + 1} - {WBK_list[i][1]}', value = f'**Tag -** {WBK_list[i][2]} \n**Date de création -** {WBK_list[i][4]}', inline = False)
                lines += 1

                if lines == 10:
                    break

            wbk_embed = discord.Embed(title = f'{interaction.user.name}\'s webhooks', description = 'Aucun webhook correspondant', color = 0x00ffff) if lines == 0 else wbk_embed
            
            await interaction.message.edit(embed = wbk_embed)
            await interaction.response.defer()

        else:
            await interaction.response.send_message(f'> Utilisez "**U!wbk_list**" pour voir votre liste...', ephemeral = True)

    @discord.ui.button(label = "...", custom_id = "reset")
    async def reset(self, interaction : discord.Interaction, button : discord.ui.Button):
        if interaction.user.id == self.Uid:
            WBK_list = WBK.get_webhooks_list(interaction.user.id) if WBK.get_webhooks_list(interaction.user.id) else []
            self.max_page = len(WBK_list)
            lines = 0
            
            self.page_id = 1
            wbk_embed = discord.Embed(title = f'{interaction.user.name}\'s webhooks - page {self.page_id}' , color = 0x00ffff)

            for i in range(len(WBK_list)):
                wbk_embed.add_field(name = f'{i + 1} - {WBK_list[i][1]}', value = f'**Tag -** {WBK_list[i][2]} \n**Date de création -** {WBK_list[i][4]}', inline = False)
                lines += 1

                if lines == 10:
                    break

            wbk_embed = discord.Embed(title = f'{interaction.user.name}\'s webhooks', description = 'Aucun webhook correspondant', color = 0x00ffff) if lines == 0 else wbk_embed

            await interaction.message.edit(embed = wbk_embed)
            await interaction.response.defer()

        else:
            await interaction.response.send_message(f'> Utilisez "**U!wbk_list**" pour voir votre liste...', ephemeral = True)

    @discord.ui.button(label = "➡️", custom_id = "right")
    async def right(self, interaction : discord.Interaction, button : discord.ui.Button):
        if interaction.user.id == self.Uid:
            WBK_list = WBK.get_webhooks_list(interaction.user.id) if WBK.get_webhooks_list(interaction.user.id) else []
            self.max_page = len(WBK_list)
            lines = 0

            if self.page_id < self.max_page:
                self.page_id += 1

            wbk_embed = discord.Embed(title = f'{interaction.user.name}\'s webhooks - page {self.page_id}' , color = 0x00ffff)

            for i in range((10 * (self.page_id - 1)), len(WBK_list)):
                wbk_embed.add_field(name = f'{i + 1} - {WBK_list[i][1]}', value = f'**Tag -** {WBK_list[i][2]} \n**Date de création -** {WBK_list[i][4]}', inline = False)
                lines += 1

                if lines == 10:
                    break

            wbk_embed = discord.Embed(title = f'{interaction.user.name}\'s webhooks', description = 'Aucun webhook correspondant', color = 0x00ffff) if lines == 0 else wbk_embed
            
            await interaction.message.edit(embed = wbk_embed)
            await interaction.response.defer()

        else:
            await interaction.response.send_message(f'> Utilisez "**U!wbk_list**" pour voir votre liste...', ephemeral = True)

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
                    await discord.StageChannel.create_webhook(self = message.channel, name = f'UnkaiWBK_{WBK_list[i][0]}')
                    WBK.set_registration(WBK_list[i][0], message.guild.id, message.guild.name)

                guild_WBK_list = await message.guild.webhooks()
                WBK_names = [elt.name for elt in guild_WBK_list]

                if f'UnkaiWBK_{WBK_list[i][0]}' in WBK_names:
                    webhook = Webhook.from_url(guild_WBK_list[WBK_names.index(f'UnkaiWBK_{WBK_list[i][0]}')].url, session = session)
                    
                    if webhook.channel != message.channel:
                        await webhook.delete()
                        webhook = await discord.StageChannel.create_webhook(self = message.channel, name = f'UnkaiWBK_{WBK_list[i][0]}')

                    await webhook.send(message.content[len(tag) :], username = WBK_list[i][1], avatar_url = WBK_list[i][3])


# base command

async def register(ctx : commands.Context, name : str, tag : str, avatar_url : str = None):
    if not check_validity(name) or not check_validity(tag):
        await ctx.send(f'Le nom et/ou le tag ne sont pas valide, opération impossible')

    else:
        result = WBK.add_webhook(name, tag, ctx.author.id, ctx.author.name, avatar_url)

        if not result:
            await ctx.send(f'Une erreur est survenue, veuillez réessayer')

        else:
            await ctx.send(f'Le webhook "**{name}**" a bien été enregistré')

async def webhooks_list(ctx : commands.Context):
    WBK_list = WBK.get_webhooks_list(ctx.author.id) if WBK.get_webhooks_list(ctx.author.id) else []
    wbk_embed = discord.Embed(title = f'{ctx.author.name}\'s webhooks - page 1' , color = 0x00ffff) if len(WBK_list) > 10 else discord.Embed(title = f'{ctx.author.name}\'s webhooks' , color = 0x00ffff)
    lines = 0

    for i in range(len(WBK_list)):
        wbk_embed.add_field(name = f'{i + 1} - {WBK_list[i][1]}', value = f'**Tag -** {WBK_list[i][2]} \n**Date de création -** {WBK_list[i][4]}', inline = False)
        lines += 1

        if lines == 10:
            break

    wbk_embed = discord.Embed(title = f'{ctx.author.name}\'s webhooks', description = 'Aucun webhook correspondant', color = 0x00ffff) if lines == 0 else wbk_embed

    await ctx.send(embed = wbk_embed, view = button_view(ctx.author.id)) if len(WBK_list) > 10 else await ctx.send(embed = wbk_embed)

async def unregister(ctx : commands.Context, name : str):
    WBK_list = WBK.get_webhooks_list(ctx.author.id)
    result = False

    for wbk in WBK_list:
        if name.lower() == wbk[1].lower():
            result = WBK.remove_webhook(wbk[0])
            break

    await ctx.send(f'Le webhook "**{name}**" a bien été supprimé') if result else await ctx.send(f'Aucun webhook corespondant, essayez "U!wbk_list"...')

async def avatar_edit(ctx : commands.Context, name : str, avatar_url : str):
    WBK_list = WBK.get_webhooks_list(ctx.author.id)
    result = False

    for wbk in WBK_list:
        if name.lower() == wbk[1].lower():
            result = WBK.edit_webhook_avatar(avatar_url, wbk[1], ctx.author.id)
            break

    await ctx.send(f'L\'avatar du webhook "**{name}**" a bien été modifié') if result else await ctx.send(f'Aucun webhook corespondant, essayez "U!wbk_list"...')

async def name_edit(ctx : commands.Context, name : str, new_name : str):
    WBK_list = WBK.get_webhooks_list(ctx.author.id)
    result = False

    for wbk in WBK_list:
        if name.lower() == wbk[1].lower():
            result = WBK.edit_webhook_name(new_name, wbk[1], ctx.author.id)
            break

    await ctx.send(f'Le nom du webhook "**{name}**" a bien été modifié en "**{new_name}**"') if result else await ctx.send(f'Aucun webhook corespondant, essayez "U!wbk_list"...')

async def tag_edit(ctx : commands.Context, name : str, new_tag : str):
    WBK_list = WBK.get_webhooks_list(ctx.author.id)
    result = False

    for wbk in WBK_list:
        if name.lower() == wbk[1].lower():
            result = WBK.edit_webhook_tag(new_tag, wbk[1], ctx.author.id)
            break

    await ctx.send(f'Le tag du webhook "**{name}**" a bien été modifié en "**{new_tag}**"') if result else await ctx.send(f'Aucun webhook corespondant, essayez "U!wbk_list"...')

async def search(ctx : commands.Context, name : str):
    WBK_list = WBK.get_webhooks_list(ctx.author.id)
    wbk_embed = discord.Embed(title = f'{ctx.author.name}\'s webhooks' , color = 0x00ffff)
    lines = 0

    for i in range(len(WBK_list)):
        if name.lower() in WBK_list[i][1].lower():
            wbk_embed.add_field(name = f'{i + 1} - {WBK_list[i][1]}', value = f'**Tag -** {WBK_list[i][2]} \n**Date de création -** {WBK_list[i][4]}', inline = False)
            lines += 1

        if lines == 24:
            wbk_embed.add_field(name = f'Essayez "U!wbk_list" pour plus de résultats', value = f'La recherche ne peut pas encore afficher plus de 24 résultats... \nEssayez "U!wbk_list" ou bien une recherche plus précise pour continuer', inline = False)
            break

    wbk_embed = discord.Embed(title = f'{ctx.author.name}\'s webhooks', description = 'Aucun webhook correspondant', color = 0x00ffff) if lines == 0 else wbk_embed
            
    await ctx.send(embed = wbk_embed)


# slash command

async def slash_register(interaction : discord.Interaction, name : str, tag : str, avatar_url : str = None): # Impossible de lier une image
    if not check_validity(name) or not check_validity(tag):
        await interaction.response.send_message(f'Le nom et/ou le tag ne sont pas valide, opération impossible')

    else:
        result = WBK.add_webhook(name, tag, interaction.user.id, interaction.user.name)

        if not result:
            await interaction.response.send_message(f'Une erreur est survenue, veuillez réessayer')

        else:
            await interaction.response.send_message(f'Le webhook "**{name}**" a bien été enregistré')

async def slash_webhooks_list(interaction : discord.Interaction):
    WBK_list = WBK.get_webhooks_list(interaction.user.id) if WBK.get_webhooks_list(interaction.user.id) else []
    wbk_embed = discord.Embed(title = f'{interaction.user.name}\'s webhooks - page 1' , color = 0x00ffff) if len(WBK_list) > 10 else discord.Embed(title = f'{interaction.user.name}\'s webhooks' , color = 0x00ffff)
    lines = 0

    for i in range(len(WBK_list)):
        wbk_embed.add_field(name = f'{i + 1} - {WBK_list[i][1]}', value = f'**Tag -** {WBK_list[i][2]} \n**Date de création -** {WBK_list[i][4]}', inline = False)
        lines += 1

        if lines == 10:
            break

    wbk_embed = discord.Embed(title = f'{interaction.user.name}\'s webhooks', description = 'Aucun webhook correspondant', color = 0x00ffff) if lines == 0 else wbk_embed

    await interaction.response.send_message(embed = wbk_embed, view = button_view(interaction.user.id)) if len(WBK_list) > 10 else await interaction.response.send_message(embed = wbk_embed)

async def slash_unregister(interaction : discord.Interaction, name : str):
    WBK_list = WBK.get_webhooks_list(interaction.user.id)

    for wbk in WBK_list:
        if name.lower() == wbk[1].lower():
            result = WBK.remove_webhook(wbk[0])
            break

    await interaction.response.send_message(f'Le webhook "**{name}**" a bien été supprimé') if result else await interaction.response.send_message(f'Aucun webhook corespondant, essayez "U!wbk_list"...')

async def slash_name_edit(interaction : discord.Interaction, name : str, new_name : str):
    WBK_list = WBK.get_webhooks_list(interaction.user.id)
    result = False

    for wbk in WBK_list:
        if name.lower() == wbk[1].lower():
            result = WBK.edit_webhook_name(new_name, wbk[1], interaction.user.id)
            break

    await interaction.response.send_message(f'Le nom du webhook "**{name}**" a bien été modifié en "**{new_name}**"') if result else await interaction.response.send_message(f'Aucun webhook corespondant, essayez "U!wbk_list"...')

async def slash_tag_edit(interaction : discord.Interaction, name : str, new_tag : str):
    WBK_list = WBK.get_webhooks_list(interaction.user.id)
    result = False

    for wbk in WBK_list:
        if name.lower() == wbk[1].lower():
            result = WBK.edit_webhook_tag(new_tag, wbk[1], interaction.user.id)
            break

    await interaction.response.send_message(f'Le tag du webhook "**{name}**" a bien été modifié en "**{new_tag}**"') if result else await interaction.response.send_message(f'Aucun webhook corespondant, essayez "U!wbk_list"...')

async def slash_search(interaction : discord.Interaction, name : str):
    WBK_list = WBK.get_webhooks_list(interaction.user.id)
    wbk_embed = discord.Embed(title = f'{interaction.user.name}\'s webhooks' , color = 0x00ffff)
    lines = 0

    for i in range(len(WBK_list)):
        if name.lower() in WBK_list[i][1].lower():
            wbk_embed.add_field(name = f'{i + 1} - {WBK_list[i][1]}', value = f'**Tag -** {WBK_list[i][2]} \n**Date de création -** {WBK_list[i][4]}', inline = False)
            lines += 1

        if lines == 24:
            wbk_embed.add_field(name = f'Essayez "U!wbk_list" pour plus de résultats', value = f'La recherche ne peut pas encore afficher plus de 24 résultats... \nEssayez "U!wbk_list" ou bien une recherche plus précise pour continuer', inline = False)
            break

    wbk_embed = discord.Embed(title = f'{interaction.user.name}\'s webhooks', description = 'Aucun webhook correspondant', color = 0x00ffff) if lines == 0 else wbk_embed
            
    await interaction.response.send_message(embed = wbk_embed)