from twitchAPI.twitch import Twitch
from twitchAPI.helper import first
import asyncio
from unkai_tk import TOKENT

async def twitch_example():
    # initialize the twitch instance, this will by default also create a app authentication for you
    twitch = await Twitch('dp04y37e220cpafyqr0z0ijvlhw444', TOKENT)
    # call the API for the data of your twitch user
    # this returns a async generator that can be used to iterate over all results
    # but we are just interested in the first result
    # using the first helper makes this easy.
    user = await first(twitch.get_users(logins='nsx_moeru'))
    # print the ID of your user or do whatever else you want with it
    print(user.id)

# run this example
asyncio.run(twitch_example())


# - - - - - - - - - - - - - - - -  I N F O R M A T I O N S  - - - - - - - - - - - - - - - - #

# > Actual version - 0
# > Uid - 4
# > Creation - 2023/11
# > Total scripts - 1