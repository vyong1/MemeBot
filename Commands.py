import SoundFile
import Filenames

sound_commands_dict = {
    '!ancestors' : SoundFile.SoundFile(Filenames.SoundsDirectory + 'MyAncestors.mp3'),
    '!balance' : SoundFile.SoundFile(Filenames.SoundsDirectory + 'BalanceInAllThings.mp3'),
    '!toby' : SoundFile.SoundFile(Filenames.SoundsDirectory + 'NoGodNo.mp3', 0.4),
    '!middle' : SoundFile.SoundFile(Filenames.SoundsDirectory + 'middle.mp3', 0.5),
    '!killmyself' : SoundFile.SoundFile(Filenames.SoundsDirectory + 'ImGoingToKillMyself.mp3', 0.5),
    '!thicc' : SoundFile.SoundFile(Filenames.SoundsDirectory + 'thicc.mp3', 0.5),
}