from discord import Intents, Status, Activity, ActivityType
from discord.ext.bridge import Bot
from config import token

intents = Intents(guilds=True, guild_messages=True, message_content=True)
# intents.message_content = True #Uncomment this if you use prefixed command that are not mentions
bot = Bot(intents=intents, command_prefix=">>", status=Status.dnd,
          activity=Activity(type=ActivityType.watching, name="you (prefix: >>)"))
bot.load_extensions("cogs")  # Loads all cogs in the cogs folder
bot.remove_command('help') # Disables the default help command
BOOTED = False


@bot.listen()
async def on_connect():
    print('Connected to Discord!')


@bot.listen()
async def on_ready():
    global BOOTED
    if BOOTED:
        print("Reconnect(?)")
    if not BOOTED:
        # await bot.sync_commands() #You might need to uncomment this if the slash commands aren't appearing
        print(f'Logged in as {bot.user}')
        print('------')
        BOOTED = True


bot.run(token)
