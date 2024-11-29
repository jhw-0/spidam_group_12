import os
import pydub
import pathlib

class Model:
    def __init__(self):
        self.audio_file = None # pathlib.Path(audio_file).resolve
        self.file_type = None # self.audio_file.suffix
        self.converted = None

    def set_audio_file(self, audio_file : str):
        self.audio_file = audio_file
    def get_name(self):
        return self.audio_file.name
    
    def check_wav(self, path : str) -> bool:
        return os.path.splitext(path)[1] == '.wav'
    
    def audio_file_button(self) -> str:
        return input('What is the path of your audio file?')
    
    # need to use pathlib.Path object, not string
    def convert_to_wav(self, path : pathlib.Path) -> str:
        supported_ext = '.mp3', '.flv', '.mp4', '.wma', '.ogg'
        
        dst = os.path.splitext(path)[0] + '.wav'
        ext = os.path.splitext(path)[1]
        if ext in supported_ext:
            pydub.AudioSegment.from_file(path, ext[1:]).export(dst, format='wav')
        else:
            print('Sorry. File type not supported. Instead, try any of: ')
            for ext in supported_ext:
                print(ext)
        return dst