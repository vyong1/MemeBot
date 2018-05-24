import discord
import asyncio
import MemeRequest
import requests
import shutil

client = discord.Client()

@client.event
async def on_message(message):
    # Handler for a message
    if message.content.startswith('!'):# Command issued
        await run_command(message)

    elif "<@448913433245646848>" in message.content: # @MemeBot
        # Get a meme from Reddit
        mc = MemeRequest.MemeRequest()
        post = mc.giveMeme()
        # Request the image and write it as a png
        url = post['url']
        # Special case for imgur links
        if "imgur" in url:
            url = url[0:8] + 'i.' + url[8:] + '.jpg'
        # vyong note: Post contains a field for 'nsfw', but is currently not used
        response = requests.get(post['url'], stream=True)
        with open('files/memepic.png', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
        await client.send_message(message.channel, post['title'])
        await client.send_file(message.channel, 'files/memepic.png')
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
