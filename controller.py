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
    
    def display_file_name(self):
        self.view.name = self.model.audio_file
    
    def load_audio_file(self):
        self.view.file_type