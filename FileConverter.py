from PIL import Image as img
import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from pydub import AudioSegment

class MyGUI:

    #The constructor for the GUI
    def __init__(self):
        self.root=tk.Tk()
        
        self.label = tk.Label(self.root, text="Select a File to convert", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)
        self.root.geometry("500x500")

        self.button=tk.Button(self.root, text="Select video file", font=('Arial',18), command=self.SelectVideoFile)
        self.button.pack(padx=10,pady=10)

        self.button=tk.Button(self.root, text="Select Audio File", font=('Arial',18), command=self.SelectAudioFile)
        self.button.pack(padx=10,pady=10)

#        self.label = tk.Label(self.root, text="You have selected: " + self.filename, font=('Arial', 20))
#        self.label.pack(padx=20, pady=20)

        self.root.mainloop()

#It is important that we have the word "self" in the parameters because we are in a class
    def SelectVideoFile(self):
        filetypes = (
            ('text files', '*.mp4'),
            ('audio files', '*.m4v'),
            ('All files', '*.*')
        )

#Since we are in a class, we need to put self in front of file name in order to properly retrieve it from our object
        self.filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

        showinfo(
            title='You Have selected:',
            message=self.filename
        )


    def SelectAudioFile(self):
        filetypes = (
            ('text files', '*.mp3'),
            ('audio files', '*.m4a'),
            ('All files', '*.*')
        )

        self.filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

        showinfo(
            title='You Have selected:',
            message=self.filename
        )



def Convert(RetrievedFile):
    
    AudioSegment.from_file(RetrievedFile).export("Output.mp3", format="mp3")


def main():
    ConstructedGUI=MyGUI()
    RetrievedFile=ConstructedGUI.filename
    Convert(RetrievedFile)


if __name__ == '__main__':
    main()
