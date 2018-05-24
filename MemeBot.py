import discord
import asyncio
import MemeRequest

client = discord.Client()

@client.event
async def on_message(message):
    # Handler for a message
    if message.content.startswith('!'):
        # Command issued
        await run_command(message)
    elif "<@448913433245646848>" in message.content:
        mc = MemeRequest.MemeRequest()
        mc.request()
        filename = mc.giveMeme()
        await client.send_file(message.channel, filename)
    elif message.content.startswith('packet'):
        await client.send_message(message.channel, "DEE-LEY")
    else:
        pass

async def run_command(message):
    # Runs a command
    if(message.content == "!logout"):
        await client.logout()
        print("Bot successfully logged out")
    else:
        await client.send_message(message.channel, "Sorry, I don't recognize that command")
    

# Start the bot
print("Bot Started")

f = open('files/token.txt', 'r')
token = f.read()
f.close()

client.run(token)
