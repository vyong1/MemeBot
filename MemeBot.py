import discord
import asyncio
import MemeRequest
import Filenames
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
            with open(Filenames.MemePicture, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response

            # Send messages
            await client.send_message(message.channel, post['title'])
            await client.send_file(message.channel, Filenames.MemePicture)
    else:
        pass

async def run_command(message):
    '''Runs a command'''
    if(message.content == "!logout"):
        await client.logout()
        print("Bot successfully logged out")
    elif(message.content == "!ancestors"):
        await play_sound_file('files/sounds/MyAncestors.mp3', message.author.voice_channel)
    elif(message.content == "!balance"):
        await play_sound_file('files/sounds/BalanceInAllThings.mp3', message.author.voice_channel)
    elif(message.content == "!toby"):
        await play_sound_file('files/sounds/NoGodNo.mp3', message.author.voice_channel, volume=0.4)
    elif(message.content == "!middle"):
        await play_sound_file('files/sounds/middle.mp3', message.author.voice_channel, volume=0.5)
    elif(message.content == "!killmyself"):
        await play_sound_file('files/sounds/ImGoingToKillMyself.mp3', message.author.voice_channel, volume=0.5)
    elif(message.content == "!jojoroll"):
        await play_sound_file('files/sounds/roll.mp3', message.author.voice_channel, volume=0.5)
    elif(message.content == "!nani"):
        await play_sound_file('files/sounds/nani.mp3', message.author.voice_channel, volume=0.2)
    elif(message.content == "!thicc"):
        await play_sound_file('files/sounds/thicc.mp3', message.author.voice_channel, volume=0.5)
    else:
        await client.send_message(message.channel, "Sorry, I don't recognize that command")
    
    sound_cmds = {
        "!ancestors" : "MyAncestors.mp3",
        "!balance" : "BalanceInAllThings.mp3",
        "!toby" : "NoGodNo.mp3",
        "!middle" : "middle.mp3",
        "!killmyself" : "ImGoingToKillMyself.mp3",
        "!roll" : "roll.mp3"
    }

async def play_sound_file(file, channel, volume=0.5):
    ''''Plays a sound file for the user'''
    # Join the channel
    voice = await client.join_voice_channel(channel)

    # Play the sound file
    player = voice.create_ffmpeg_player(file)
    player.volume = volume
    player.start()

    # Wait until the sound clip is finished before leaving
    while(not player.is_done()):
        pass
    await voice.disconnect()

# Start the bot
print("Bot Started")

f = open(Filenames.Token, 'r')
token = f.read()
f.close()

client.run(token)
