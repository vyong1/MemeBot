import discord
import asyncio
import MemeRequest
import requests
import shutil
import time

client = discord.Client()

@client.event
async def on_message(message):
    '''Handler for a message'''
    if message.content.startswith('!'):# Command issued
        await run_command(message)

    elif "<@448913433245646848>" in message.content: # @MemeBot
        # Get a meme from Reddit
        mc = MemeRequest.MemeRequest()
        post = mc.giveMeme()
        # vyong note: Post contains a field for 'nsfw', but is currently not used

        # Request the image and write it as a png
        url = post['url']
        while ('www.' in url):
            # Special case for reddit non-image posts - get another meme
            post = mc.giveMeme()
            url = post['url']

        # Special case for non-reddit links
        if not("i.redd.it" in url):
            await client.send_message(message.channel, post['title'])
            await client.send_message(message.channel, url)
        else:
            # Request the image
            response = requests.get(post['url'], stream=True)

            # Write the image data into files/memepic.png
            with open('files/memepic.png', 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response

            # Send messages
            await client.send_message(message.channel, post['title'])
            await client.send_file(message.channel, 'files/memepic.png')
    else:
        pass

async def run_command(message):
    '''Runs a command'''
    if(message.content == "!logout"):
        await client.logout()
        print("Bot successfully logged out")
    elif(message.content == "!ancestors"):
        await play_sound_file('files/sounds/MyAncestors.mp3')
    elif(message.content == "!balance"):
        await play_sound_file('files/sounds/BalanceInAllThings.mp3')
    elif(message.content == "!takeonme"):
        await play_sound_file('files/sounds/TakeOnMe.mp3')
    else:
        await client.send_message(message.channel, "Sorry, I don't recognize that command")

async def play_sound_file(file):
    ''''Plays a sound file for the user'''
    # Join the channel
    channel = client.get_channel('416087631043100673')
    voice = await client.join_voice_channel(channel)

    # Play the sound file
    player = voice.create_ffmpeg_player(file)
    player.volume = 0.5
    player.start()

    # Wait until the sound clip is finished before leaving
    while(not player.is_done()):
        pass
    await voice.disconnect()

# Start the bot
print("Bot Started")

f = open('files/token.txt', 'r')
token = f.read()
f.close()

client.run(token)
