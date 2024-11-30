import pydub
import pathlib

class Model:
    def __init__(self):
        self._audio_file_path = None
        self._audio_file = None
    
    supported_file_extensions = '.mp3', '.flv', '.mp4', '.wma', '.ogg'

    # _audio_file_path --------------------------------------------------------
    @property
    def audio_file_path(self) -> pathlib.Path:
        return self._audio_file_path
    
    @audio_file_path.setter
    def audio_file_path(self, audio_file_path : str) -> None:
        # first, sets the property
        self._audio_file_path = pathlib.Path(audio_file_path).resolve()

        # second, presets the audio_file property conditionally

        # don't allow program to run with an unsupported file type
        if not self._audio_file_path.suffix in Model.supported_file_extensions:
            print('Sorry. File type not supported. Instead, try any of: ')
            for extension in Model.supported_file_extensions:
                print(extension, end=' ')
        # pre-setting the audio_file attribute
        else:
            self._load_audio_file()

    # -------------------------------------------------------------------------


    # _audio_file -------------------------------------------------------------
    @property
    def audio_file(self) -> pydub.audio_segment.AudioSegment:
        return self._audio_file
    
    # -------------------------------------------------------------------------
    

    # _load_audio_file and helping functions ----------------------------------
    # this is called (preset) by the audio_file_path setter
    def _load_audio_file(self) -> None:
        # setting audio_file
        self._audio_file = pydub.AudioSegment.from_file(
            self._audio_file_path,
            format=self._audio_file_path.suffix[1:] # `[1:]` to remove `.`
        )
        print(f'Successfully loaded the audio_file as {self._audio_file}')
        # below, processing audio_file to be usable

        # export to wav conditionally
        if not self._check_if_wav() or self._check_meta():
            self._export_to_wav()
        
        # convert to one channel audio
        if not self._check_if_one_channel():
            self._convert_to_one_channel()

    def _check_if_wav(self) -> bool:
        return self.audio_file_path.suffix == '.wav'
    
    def _export_to_wav(self) -> str:
        # resetting the _audio_file attribute
        self._audio_file.export(
            # caches the audio file next to the old one on the file sys
            destination := self.audio_file_path.with_suffix('.wav'),
            format='wav'
        )
        print(f'Successfully exported the audio_file as {self._audio_file}')

        # resetting the _audio_file_path attribute
        self._audio_file_path = destination

        # resetting the _audio_file attribute
        self._audio_file_path = pydub.AudioSegment.from_file(
            self._audio_file_path,
            format='wav'
        )

    def _check_meta(self) -> bool:
        return bool(pydub.utils.mediainfo(str(self._audio_file)).get('TAG'))
    
    def _check_if_one_channel(self) -> bool:
        print(self._audio_file)
        print(type(self._audio_file))
        return self._audio_file.channels == 1

    def _convert_to_one_channel(self) -> None:
        # resetting the _audio_file attribute
        self._audio_file = self._audio_file.set_channels(1)

    # -------------------------------------------------------------------------
