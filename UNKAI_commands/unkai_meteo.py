from discord import *
import discord 
from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord.ext.commands import has_permissions
from discord.shard import EventType
from discord import app_commands
from nacl import *
from time import *
from random import randint, choice

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix = 'U!', description = 'narrateur rp', intents = intents)


# météo - v2

def temperature(climate_id : int, season_id : int):
    temp_min, temp_max = 0, 0

    # Définition des températures de base par climat (climate_id)
    if climate_id == 1: # - Climat montagnard
        temp_min, temp_max = -20, -5

    elif climate_id == 2: # - Climat froid
        temp_min, temp_max = -10, 10

    elif climate_id == 3: # - Climat tempéré
        temp_min, temp_max = 5, 25
    
    elif climate_id == 4: # - Climat chaud
        temp_min, temp_max = 20, 40

    elif climate_id == 5: # - Climat aride
        temp_min, temp_max = 35, 45

    else: # - Temérature moyenne (hors climat)
        temp_min, temp_max = 0, 30

    # Adaptation des bornes de base selon la saison (season_id)
    if season_id == 1: # - Printemps
        temp_min -=  0.12 * temp_min
        temp_max -= -0.12 * temp_max

    elif season_id == 2: # - Été
        temp_min -= -0.24 * temp_min
        temp_max -= -0.21 * temp_max

    elif season_id == 3: # - Automne
        temp_min -= 0.15 * temp_min
        temp_max -= -0.12 * temp_max

    elif season_id == 4: # - Hiver
        temp_min -= 0.24 * temp_min
        temp_max  -= 0.27 * temp_max 

    # Renvoie des bornes calculées
    return [temp_min, temp_max]

def temp_update(temp_min : float = 0, temp_max : float = 30, last_temp : float = None):
    temp = 0

    # Cas par défaut
    if temp_min == temp_max: # Bornes identiques
        temp = temp_min

    elif last_temp == None: # Pas de référentiel
        temp = randint(int(temp_min + 1), int(temp_max - 1))

    else:
        temp_m = (temp_min + temp_max) / 2
        update_values = [0.1 * randint(2, 24), -0.1 * randint(2, 24)]
        value = choice(update_values)

        # Application de la valeur de changement
        if (last_temp < temp_m and value < 0) or (last_temp > temp_m and value > 0):
            value = 0.85 * value

        temp = last_temp + value

    # Renvoie de la nouvelle température 
    return round(temp, 1)

def weather(climate_id : int, season_id : int, temp : float):
    final_weather = 0
    weather_list = ['🌪️ - venté', '☀️ - ensoleillé', '☁️ - nuageux', '🌩️ - orageux', '⛈️ - orageux et pluvieux', '🌧️ - pluvieux', '🌨️ - neigeux', '🌊 - tempête'] # ID - 0 à 7
    base = randint(0, 100)

    # Adaptation des probabilités selon la saison (season_id)
    if season_id == 1: # - Printemps
        # Températures négatives
        if temp <= 0 and base < 20:
            final_weather = 0 # venté

        elif temp <= 0 and 20 <= base < 60:
            final_weather = 6 # neigeux

        elif temp <= 0 and 60 <= base < 65:
            final_weather = 3 # orageux

        elif temp <= 0 and 65 <= base < 80:
            final_weather = 2 # nuageux

        elif temp <= 0 and base > 80:
            final_weather = 1 # ensoleillé

        # Températures positives
        if temp > 0 and base < 18:
            final_weather = 0 # venté

        elif temp > 0 and 18 <= base < 38:
            final_weather = 7 if climate_id == 5 else 5 # pluvieux (ou tempête si aride)

        elif temp <= 0 and 38 <= base < 46:
            final_weather = 4 # orageux et pluvieux

        elif temp <= 0 and 46 <= base < 52:
            final_weather = 3 # orageux

        elif temp > 0 and 52 <= base < 75:
            final_weather = 2 # nuageux

        elif temp > 0 and base > 75:
            final_weather = 1 # ensoleillé

    elif season_id == 2: # - Été
        # Températures négatives
        if temp <= 0 and base < 24:
            final_weather = 0 # venté

        elif temp <= 0 and 24 <= base < 42:
            final_weather = 6 # neigeux

        elif temp <= 0 and 42 <= base < 55:
            final_weather = 3 # orageux

        elif temp <= 0 and 55 <= base < 78:
            final_weather = 2 # nuageux

        elif temp <= 0 and base > 78:
            final_weather = 1 # ensoleillé

        # Températures positives
        if temp > 0 and base < 12:
            final_weather = 0 # venté

        elif temp > 0 and 12 <= base < 28:
            final_weather = 7 if climate_id == 5 else 5 # pluvieux (ou tempête si aride)

        elif temp <= 0 and 28 <= base < 35:
            final_weather = 4 # orageux et pluvieux

        elif temp <= 0 and 35 <= base < 48:
            final_weather = 3 # orageux

        elif temp > 0 and 48 <= base < 70:
            final_weather = 2 # nuageux

        elif temp > 0 and base > 70:
            final_weather = 1 # ensoleillé

    elif season_id == 3: # - Automne
        # Températures négatives
        if temp <= 0 and base < 25:
            final_weather = 0 # venté

        elif temp <= 0 and 25 <= base < 68:
            final_weather = 6 # neigeux

        elif temp <= 0 and 68 <= base < 74:
            final_weather = 3 # orageux

        elif temp <= 0 and 74 <= base < 85:
            final_weather = 2 # nuageux

        elif temp <= 0 and base > 85:
            final_weather = 1 # ensoleillé

        # Températures positives
        if temp > 0 and base < 18:
            final_weather = 0 # venté

        elif temp > 0 and 18 <= base < 40:
            final_weather = 7 if climate_id == 5 else 5 # pluvieux (ou tempête si aride)

        elif temp <= 0 and 40 <= base < 48:
            final_weather = 4 # orageux et pluvieux

        elif temp <= 0 and 48 <= base < 55:
            final_weather = 3 # orageux

        elif temp > 0 and 55 <= base < 78:
            final_weather = 2 # nuageux

        elif temp > 0 and base > 78:
            final_weather = 1 # ensoleillé

    elif season_id == 4: # - Hiver
        # Températures négatives
        if temp <= 0 and base < 20:
            final_weather = 0 # venté

        elif temp <= 0 and 20 <= base < 48:
            final_weather = 6 # neigeux

        elif temp <= 0 and 48 <= base < 60:
            final_weather = 3 # orageux

        elif temp <= 0 and 60 <= base < 78:
            final_weather = 2 # nuageux

        elif temp <= 0 and base > 78:
            final_weather = 1 # ensoleillé

        # Températures positives
        if temp > 0 and base < 25:
            final_weather = 0 # venté

        elif temp > 0 and 25 <= base < 42:
            final_weather = 5 # pluvieux

        elif temp <= 0 and 42 <= base < 50:
            final_weather = 4 # orageux et pluvieux

        elif temp <= 0 and 50 <= base < 58:
            final_weather = 3 # orageux

        elif temp > 0 and 58 <= base < 82:
            final_weather = 2 # nuageux

        elif temp > 0 and base > 82:
            final_weather = 1 # ensoleillé

    # Renvoie des bornes calculées
    return [weather_list[final_weather], final_weather]


# base command

async def meteo(ctx : commands.Context, nom : str, climat : int, saison : int, durée : int, last_temp : float):
    meteo_embed = discord.Embed(title = nom, color = 0x00ffff)
    bornes_temperatures = temperature(climat, saison)
    temp = last_temp

    for i in range(durée):
        temp = temp_update(bornes_temperatures[0], bornes_temperatures[1], temp) 
        temps = weather(climat, saison, temp)
        meteo_embed.add_field(name = f'Jour {i + 1}', value = f'{temps[0]} - *{temp}°C*', inline = False)

    await ctx.send(embed = meteo_embed)
    await ctx.message.delete()


# slash command

async def slash_meteo(interaction : discord.Interaction, nom : str, climat : int, saison : int, durée : int, last_temp : float):
    meteo_embed = discord.Embed(title = nom, color = 0x00ffff)
    bornes_temperatures = temperature(climat, saison)
    temp = last_temp

    for i in range(durée):
        temp = temp_update(bornes_temperatures[0], bornes_temperatures[1], temp) 
        temps = weather(climat, saison, temp)
        meteo_embed.add_field(name = f'Jour {i + 1}', value = f'{temps[0]} - *{temp}°C*', inline = False)

    await interaction.response.send_message(embed = meteo_embed)