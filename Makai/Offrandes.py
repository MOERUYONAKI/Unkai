# - - - - - - - - - - - - - - - -  I M P O R T S  - - - - - - - - - - - - - - - - #


from discord import *
import discord 
from discord.ext import commands


# - - - - - - - - - - - - - - - -  A U T R E S  - - - - - - - - - - - - - - - - #


intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix = 'U!', description = 'narrateur rp', intents = intents)


# - - - - - - - - - - - - - - - -  C O M M A N D E S  - - - - - - - - - - - - - - - - #


async def offrande(interaction : discord.Interaction, type : app_commands.Choice[int], lien : str):
    if lien.startswith('https://discord.com/channels/1101138795446935643/'):
        if interaction.guild.id == 1101138795446935643 and interaction.user.get_role(1141359392999100416):
            if type.value == 0:
                await interaction.response.send_message(f'***Une Nébuleuse vous observant offre 100 pièces en soutien...***\n> {lien}')

            elif type.value == 1:
                await interaction.response.send_message(f'***Une Nébuleuse est impressionnée par une action et offre 500 pièces...***\n> {lien}')

            elif type.value == 2:
                await interaction.response.send_message(f'***Une Nébuleuse est subjuguée par une action et offre 1000 pièces...***\n> {lien}')

        else:
            await interaction.response.send_message(f'> Cette commande n\'est pas valable en dehors de MAKAI...', ephemeral = True)
    
    else:
        await interaction.response.send_message(f'> Ce lien n\'est pas valide...', ephemeral = True)