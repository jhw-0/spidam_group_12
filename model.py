import os
import pydub
import pathlib

class Model:
    def __init__(self):
        self._audio_file_path = None
        self._audio_file = None
        self._file_type = None
        self._new_audio_file_path = None
        self._new_audio_file = None
        self._new_file_type = None

    @property
    def audio_file_path(self) -> str:
        return str(self._audio_file)
    
    @audio_file_path.setter
    def audio_file(self, audio_file_path : str) -> None:
        # first, sets the property
        self._audio_file_path = pathlib.Path(audio_file_path).resolve()

        # second, presets the audio_file property
        self.audio_file(audio_file_path)

    @property
    def audio_file(self) -> pydub.audio_segment.AudioSegment:
        return self._audio_file
    
    # this is called (preset) by the audio_file_path setter
    @audio_file.setter
    def audio_file(
            self,
            audio_file_path : str
        ) -> None:
        self._audio_file = pydub.AudioSegment.from_file(
            self._audio_file_path,
            format='wav'
        )

        # below, audio_file is processed to be usable

        if not self._check_if_wav():
            pass
        # exporting to remove metadata is pointless if exported previously
        elif self._check_meta():
            pass
        
        # convert to one channel audio
        if not self._check_if_one_channel():
            pass



    # this function helps the audio_file setter
    def _check_if_wav(self) -> bool:
        return self.audio_file.suffix == '.wav'
    
    # this function helps the audio_file setter
    def _convert_to_wav(self) -> None:
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
                print(extension, end=' ')

    def audio_file_button(self) -> str:
        return input('What is the path of your audio file?')
    

    def _check_meta(self) -> bool:
        return bool(pydub.utils.mediainfo(str(self.audio_file)).get('TAG'))

    def check_two_channel(self) -> bool:
        channels = pydub.utils.mediainfo(str(self.audio_file)).get('channels')
        return int(channels) != 1

    def convert_to_one_channel(self) -> None:
        pass

    def remove_meta(self):
        pass