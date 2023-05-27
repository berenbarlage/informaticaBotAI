import discord
from discord.ext import commands

TOKEN = 'MTA5NTczMDQ3ODMyNzI3OTcyMA.GrwORH.sDOXylbznFtkFS4WynAffbYR5knUHeiyYHg5DQ'

intents = discord.Intents.default()
intents.typing = False

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print('Bot is klaar')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    print(message.author, message.content, message.channel.id)
    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    channel = bot.get_channel(1097514137854164992)
    await channel.send(f'Hallo daar, {ctx.author.mention}!')

bot.run(TOKEN)


