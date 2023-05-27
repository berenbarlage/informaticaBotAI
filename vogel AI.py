import discord

class MyBot(discord.Client):
    async def on_ready(self):
        print(f"Logged in as {self.user}!")

    async def on_message(self, message):
            if message.author == self.user:
                return

            if message.content.startswith("hallo"):
                await message.channel.send("hoi, ik ben de COCO bot, als je hier een foto van je vogel instuurt kijk ik voor je welke soort het is")

            if message.content.startswith("help"):
                await message.channel.send("dit is de COCO bot hulpdesk."
                                           "dit zijn de dingen waarmee de COCO bot u kan helpen "
                                           " 1. fotos van vogels herkennen en onderscheiden. "
                                           " 2. leuk terug reageren op hallo")

            if message.content.startswith("welke vogelsoort is dit?"):
                if message.attachments:
                    await message.channel.send("bedankt voor het sturen van de foto, ik ga het nu 'uitvogelen'!")
                else:
                    await message.channel.send("stuur een foto bij het bericht 'welke vogelsoort is dit?' .")




intents = discord.Intents.all()
client = MyBot(intents=intents)
client.run("MTA5NTczMDQ3ODMyNzI3OTcyMA.GMfLgw.G-jH1eMryuFBUAYWoAM1t4YZxuqUKBH0outTIY")


