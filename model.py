import os
import pydub
import pathlib

class Model:
    def __init__(self):
        self.audio_file = None
        self.original_file_type = None
        self.new_audio_file = None

    def set_audio_file(self, audio_file : str):
        self.audio_file = audio_file

    def get_name(self):
        return self.audio_file.name
    
    def check_wav(self) -> bool:
        return self.audio_file == '.wav'
    
    def audio_file_button(self) -> str:
        return input('What is the path of your audio file?')
    
    def convert_to_wav(self) -> None:
        # tuple representing supported extensions for file type conversion
        supported_extensions = '.mp3', '.flv', '.mp4', '.wma', '.ogg'
        self.original_file_type = self.audio_file.suffix
        if self.original_file_type in supported_extensions:
            pydub.AudioSegment.from_file(
                self.audio_file,
                extension
            ).export(
                destination := self.audio_file.with_suffix('.wav'),
                format='wav'
            )
            self.new_audio_file = destination
        else:
            print('Sorry. File type not supported. Instead, try any of: ')
            for extension in supported_extensions:
                print(extension)

    def check_meta(self) -> bool:
        pass

    def check_two_channel(self) -> bool:
        pass

    def convert_to_one_channel(self) -> None:
        pass

    def remove_meta(self):
        pass
        