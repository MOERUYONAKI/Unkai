from discord import *
import discord 
from discord.ext import commands
import discord.ext.commands
import discord.ext
from discord.ext.commands.bot import Bot
from discord.ext.commands import has_permissions
from discord.shard import EventType
from discord import app_commands
from nacl import *
from time import *
import asyncio
import random
import UNKAI_commands.Ressources.music_selector as selector

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix = 'U!', description = 'narrateur rp', intents = intents)

serveurs = {}
for discord_guild in bot.guilds:
    serveurs[discord_guild.id] = []

ffmpeg = 'C:\\msys64\\ffmpeg-7.0.1\\ffmpeg.exe'

async def next(voice_client : discord.VoiceClient): # lance la première musique de la queue (fonctionnel)
    def after_playing(error):
        if error:
            print(f'Erreur : {error}')
        else:
            asyncio.run(next(voice_client))

    if voice_client.guild.id not in serveurs.keys() or len(serveurs[voice_client.guild.id]) == 0:
        await voice_client.disconnect()

    else:
        song = serveurs[voice_client.guild.id].pop(0)
        voice_client.play(FFmpegPCMAudio(source = song[0]["path"], executable = ffmpeg), after = after_playing)
        print(f'Now playing - {song[0]["title"]}')


# base command

async def play(ctx : commands.Context, song_name : str, artist : str = None): # joue la musique demandée dans un salon vocal (fonctionnel)
    def after_playing(error):
        if error:
            print(f'Erreur : {error}')
        else:
            asyncio.run(next(ctx.voice_client))

    channel = ctx.author.voice.channel
    song = selector.song_select(song_name, artist)

    try: 
        await channel.connect() 
    except: 
        pass

    if song[1] >= 0.5:
        if not ctx.voice_client.is_playing():
            ctx.voice_client.play(FFmpegPCMAudio(source = song[0]["path"], executable = ffmpeg), after = after_playing)
            print(f'Now playing - {song[0]["title"]}')
        
        else:
            if ctx.guild.id in serveurs.keys():
                serveurs[ctx.guild.id].append(song)

            else:
                serveurs[ctx.guild.id] = [song]

        await ctx.message.add_reaction('✅')
    
    else:
        await ctx.send(f'Nom invalide')

async def queue(ctx : commands.Context): # passe à la musique suivante (fonctionnel)
    if ctx.guild.id in serveurs.keys() and len(serveurs[ctx.guild.id]) > 0:
        embed = discord.Embed(color = 0x00ffff)
        embed.set_author(name = f"Queue - {ctx.guild.name}", icon_url = ctx.guild.icon.url) if ctx.guild.icon != None else embed.set_author(name = f"Queue - {ctx.guild.name}")

        for elt in serveurs[ctx.guild.id]:
            if serveurs[ctx.guild.id].index(elt) < 10:
                artists = ''
                for art in elt[0]["artists"]:
                    artists += f'{art}, '

                embed.add_field(name = f"```{serveurs[ctx.guild.id].index(elt) + 1}.``` {elt[0]['title']}", value = f"> {artists[0 : -2]}", inline = False)

        await ctx.send(embed = embed)

    else:
        await ctx.send(f'> La queue est vide...')

async def skip(ctx : commands.Context): # passe à la musique suivante (fonctionnel)
    if ctx.voice_client != None:
        ctx.voice_client.stop()

async def stop(ctx : commands.Context): # arrête la musique et quitte le salon vocal (fonctionnel)
    if ctx.voice_client != None:
        serveurs[ctx.guild.id] = []
        await ctx.voice_client.disconnect()


# slash command

async def slash_play(interaction : discord.Interaction, song_name : str, artist : str = None): # joue la musique demandée dans un salon vocal (fonctionnel)
    def after_playing(error):
        if error:
            print(f'Erreur : {error}')
        else:
            asyncio.run(next(interaction.user.guild.voice_client))

    channel = interaction.user.voice.channel
    song = selector.song_select(song_name, artist)

    try: 
        await channel.connect() 
    except: 
        pass

    if song[1] >= 0.5:
        if not interaction.user.guild.voice_client.is_playing():
            interaction.user.guild.voice_client.play(FFmpegPCMAudio(source = song[0]["path"], executable = ffmpeg), after = after_playing)
            print(f'Now playing - {song[0]["title"]}')
        
        else:
            if interaction.user.guild.id in serveurs.keys():
                serveurs[interaction.user.guild.id].append(song)

            else:
                serveurs[interaction.user.guild.id] = [song]

        artists = ''
        for elt in song[0]["artists"]:
            artists += f'{elt}, '

        await interaction.response.send_message(f'> "**{song[0]["title"]} - {artists[0 : -2]}**" a été ajouté avec succès à la file d\'attente', ephemeral = True)
    
    else:
        await interaction.response.send_message(f'Nom invalide', ephemeral = True)

async def slash_queue(interaction : discord.Interaction): # passe à la musique suivante (fonctionnel)
    if interaction.user.guild.id in serveurs.keys() and len(serveurs[interaction.user.guild.id]) > 0:
        embed = discord.Embed(color = 0x00ffff)
        embed.set_author(name = f"Queue - {interaction.user.guild.name}", icon_url = interaction.user.guild.icon.url) if interaction.user.guild.icon != None else embed.set_author(name = f"Queue - {interaction.user.guild.name}")

        for elt in serveurs[interaction.user.guild.id]:
            if serveurs[interaction.user.guild.id].index(elt) < 10:
                artists = ''
                for art in elt[0]["artists"]:
                    artists += f'{art}, '

                embed.add_field(name = f"```{serveurs[interaction.user.guild.id].index(elt) + 1}.``` {elt[0]['title']}", value = f"> {artists[0 : -2]}", inline = False)

        await interaction.response.send_message(embed = embed)

    else:
        await interaction.response.send_message(f'> La queue est vide...', ephemeral = True)

async def slash_skip(interaction : discord.Interaction): # passe à la musique suivante (fonctionnel)
    if interaction.user.guild.voice_client != None:
        interaction.user.guild.voice_client.stop()

        await interaction.response.send_message(f'> La musique a été passée avec succès...', ephemeral = True)

async def slash_stop(interaction : discord.Interaction): # arrête la musique et quitte le salon vocal (fonctionnel)
    if interaction.user.guild.voice_client != None:
        serveurs[interaction.guild.id] = []

        await interaction.user.guild.voice_client.disconnect()
        await interaction.response.send_message(f'> Déconnexion, la file d\'attente a été supprimée...', ephemeral = True)