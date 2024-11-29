import os
import pydub
import pathlib
import model
import view

class Controller:
    def __init__(self, model : model.Model, view : view.View):
        # Load audio file button (placeholder)
        self.model = model
        self.view = view
    
    def display_file_name(self) -> None:
        # to do: use regexp (or other pattern matching) to ensure input is path
        self.view.name = self.model.audio_file
    
    def load_audio_file(self) -> None:
        self.model.set_audio_file(self.view.file_name_input())