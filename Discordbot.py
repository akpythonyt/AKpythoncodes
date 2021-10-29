import discord
import randfacts
x = randfacts.get_fact()
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, Rfact):
        if Rfact.content == '$fact':
            await Rfact.channel.send((x))
client = MyClient()
client.run('Token')