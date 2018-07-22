import discord
import asyncio
import MemeRequest
import Filenames
import Commands
import SoundFile
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
    '''
    Run a command.
    Commands are messages that start with '!'
    '''
    # Sound commands
    if message.content in Commands.sound_commands_dict:
        soundfile = Commands.sound_commands_dict[message.content]
        await soundfile.play(client, message.author.voice_channel)
    # Other commands
    else:
        if(message.content == "!logout"): # Log out the bot
            await client.logout()
            print("Bot successfully logged out")
        elif(message.content == "!ExecuteOrder66"): # Messages @phteven 20 times
            u = await client.get_user_info("118176521671278595")
            for i in range(0, 20):
                await client.send_message(message.channel, u.mention)
                time.sleep(0.1)
        else:
            await client.send_message(message.channel, "Sorry, I don't recognize that command")

print("Bot Started")

# Read the token
f = open(Filenames.Token, 'r')
token = f.read()
f.close()

# Start the bot
client.run(token)