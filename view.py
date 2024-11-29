import os
import pydub
import pathlib

class View:
    def __init__(self):
        pass

    def refresh(self):
        pass

    def file_name_input(self) -> str:
        pass
    
class TerminalView(View):
    def __init__(self):
        super.__init__()

    def file_name_input(self) -> str:
        return input("Please enter your audio file's name.")
    
    # should include enough information for debugging
    def refresh(self, dict):
        for key, value in dict:
            print(f'{key}: {value}')
    

class GuiView(View):
    def __init__(self):
        super.__init__()