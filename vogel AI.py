import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False


bot = commands.Bot(command_prefix='!', intents=intents)

# opstarten van de bot
@bot.event
async def on_ready():
    print('Bot is ingelogd als {0.user}'.format(bot))

# ontvangen van berichten
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Bericht
    if message.content:
        await message.channel.send(f'Je hebt een bericht gestuurd ')

    # Foto's
    if len(message.attachments) > 0:
        for attachment in message.attachments:
            await attachment.save(attachment.filename)
            await message.channel.send(f'Je hebt een foto gestuurd')

    await bot.process_commands(message)




bot.run('MTA5NTczMDQ3ODMyNzI3OTcyMA.GrwORH.sDOXylbznFtkFS4WynAffbYR5knUHeiyYHg5DQ')




