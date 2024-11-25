import os
import pydub
from pathlib import Path

def audio_file_button():
    return input('What is the path of your audio file?')

def display_file_name():
    pass

# check if path ends with .wav
def check_wav(path : str) -> bool:
    return os.path.splitext(path)[1] == '.wav'

# need to convert to .wav for scipy support
def convert_to_wav(path):
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
    

if True: #__name__ == '__main__':
    path = './audio_files/test.ogg'
    path = Path(path).resolve()
    convert_to_wav(path)