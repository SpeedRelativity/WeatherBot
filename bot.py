import discord
import weather_app

async def send_message(message, user_message):
    try:
        response = weather_app.message
        await message.channel.send(response)
    except Exception as e:
        print(e)

def run_bot():
    bot_token = ""#TOKEN GOES HERE

    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content == "!weather":
            await send_message(message, message.content)

    client.run(bot_token)

