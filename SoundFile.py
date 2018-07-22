class SoundFile:
    '''
    A class representing a sound file
    '''
    def __init__(self, filepath, volume=1):
        self.filepath = filepath
        self.volume = volume

    async def play(self, client, channel):
        '''Plays a sound file for the user'''
        # Join the channel
        voice = await client.join_voice_channel(channel)

        # Play the sound file
        player = voice.create_ffmpeg_player(self.filepath)
        player.volume = self.volume
        player.start()

        # Wait until the sound clip is finished before leaving
        while(not player.is_done()):
            pass
        await voice.disconnect()