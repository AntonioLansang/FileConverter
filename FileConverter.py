from PIL import Image as img
import os
import tkinter as tk

def main():
   
#This is the basic logic that we want to do.
# Now we just need to implement tkinter to make it cool
  #  Source=img.open(r'/Users/antoniolansang/Downloads/TestFolder/20230531_115032(1).jpg')
   # Source.save(r'/Users/antoniolansang/Downloads/TestFolder/test.png')

    root = tk.Tk()

    #Sets the width and height of a Window
    root.geometry("800x500")

    #Sets the titlebar name
    root.title("File Conversion")


    label = tk.Label(root, text="Hello", font=('Arial', 18))
    label.pack()


    textbox=tk.Text(root, height=3, font=('Arial', 16))
    textbox.pack()

    root.mainloop()
if __name__ == '__main__':
    main()
