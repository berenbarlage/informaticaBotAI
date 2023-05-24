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

    if message.attachments:
        for attachment in message.attachments:
            await attachment.save(attachment.filename)
            print(f'Ontvangen bijlage: {attachment.filename}')

    await bot.process_commands(message)


bot.run(TOKEN)

