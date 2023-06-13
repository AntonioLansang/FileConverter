from PIL import Image as img
import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo


class MyGUI:

    def __init__(self):
        self.root=tk.Tk()
        
        self.label = tk.Label(self.root, text="Message", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.textbox=tk.Text(self.root, font=('Arial', 8))
        self.textbox.pack(padx=10,pady=10)

        self.check_state= tk.IntVar()
        

        self.check=tk.Checkbutton(self.root, text="Show", font=('Arial', 20), variable=self.check_state)
        self.check.pack(padx=20,pady=20)
       

        self.button=tk.Button(self.root, text="Show Message", font=('Arial',18), command=self.show_message)
        self.button.pack(padx=10,pady=10)


        self.root.mainloop()


    def show_message(self):
        print("hello")

MyGUI()
