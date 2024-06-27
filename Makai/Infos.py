# - - - - - - - - - - - - - - - -  I M P O R T S  - - - - - - - - - - - - - - - - #


from discord import *
import discord 
from discord.ext import commands


# - - - - - - - - - - - - - - - -  A U T R E S  - - - - - - - - - - - - - - - - #


intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix = 'U!', description = 'narrateur rp', intents = intents)


# - - - - - - - - - - - - - - - -  C O M M A N D E S  - - - - - - - - - - - - - - - - #


async def makai_def(interaction : discord.Interaction, sujet : app_commands.Choice[int]):
    if sujet.value == 1: # Jugement de plausibilité
        await interaction.response.send_message(f'__**Jugement de plausibilité**__' + "\n \n" + 
                                                f"Le **jugement de plausibilité** est une réunion des Nébuleuses au sujet d'un choix, d'une action ou d'une conséquence. Le but de ce jugement est de débattre sur la possibilité que ce sujet ait lieu ou si, au contraire, cela semble irréalisable. Lorsque ce jugement est demandé par un joueur, il peut être amené à débattre sur le sujet pour défendre ses idées, mais ce n’est pas nécessairement le cas. Le résultat du jugement de plausibilité est incontestable et ne peut en aucun cas être réutilisé pour un autre cas même similaire." + "\n \n" + 
                                                f"Il est possible de demander un **jugement de plausibilité** dans plusieurs cas, comme la préparation d’une action complexe ou aux conséquences importantes, mais aussi si une action à notre encontre nous semble incohérente. Le jugement apportera dans ces situations un “laissez passer” ou bien un arrêt pouvant aller jusqu’à un “changement de destin”, soit la suppression d’une action ou sa modification. Outre cela, les Nébuleuses peuvent aussi décider d’en faire un en secret si une action leur semble non plausible ou contre le règlement.")

    elif sujet.value == 2: # Sélection du destin
        await interaction.response.send_message(f'__**Sélection du destin**__' + "\n \n" + 
                                                f'La **sélection du destin** est un choix imposé au joueur ayant des conséquences particulièrement importantes sur l’avenir de son personnage. La principale et plus commune est celle de la mort. Une telle sélection peut venir des Nébuleuses mais aussi du scénario de l’histoire ou bien simplement de vos actions, comme pour la mort. Les options de la sélection sont imposées et ne peuvent être évitées ou arrangées.')