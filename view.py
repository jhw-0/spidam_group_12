import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # load audio file button
        self._load_audio_file = ttk.Button(
            self,
            text='Load audio file',
            command=self.audio_file_button_clicked
        )
        self._load_audio_file.grid(row=1, column=1)

        # placeholder for displaying name of file
        self._name_of_file = ttk.Label(self, text=None)
        self._name_of_file.grid(row=1, column=2)

        # optional status information
        self._optional_status_info = ttk.Label(self, text=None)
        self._optional_status_info.grid(row=2, column=1)

    # to implement: for refreshing view from model ----------------------------
    def refresh(self):
        pass
    
    # -------------------------------------------------------------------------


    # audio_file_button_clicked -----------------------------------------------
    def audio_file_button_clicked(
            self,
            filetypes=(('wav files', '*.wav'), )
        ) -> str:

        filename = filedialog.askopenfilename(
            title='Open an audio file',
            initialdir='/',
            filetypes=filetypes
        )

        messagebox.showinfo(
            title='Selected file:',
            message=filename
        )

        self._name_of_file['text'] = filename

        return filename

    # -------------------------------------------------------------------------

if __name__ == '__main__':
    main_frame = tk.Tk()
    view = View(main_frame)
    view.grid(row=0, column=0, padx=10, pady=10)
    main_frame.mainloop()


#class GuiView(View, tkinter.ttk.Frame):
#    def __init__(self):
#        super.__init__()
#
#class TerminalView(View):
#    def __init__(self, parent):
#        super.__init__(parent)
#
#    def file_name_input(self) -> str:
#        return input("Please enter your audio file's name.")
#    
#    # this should include enough information for debugging
#    def refresh(self, dict):
#        for key, value in dict:
#            print(f'{key}: {value}')