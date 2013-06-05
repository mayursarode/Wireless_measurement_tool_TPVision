from Tkinter import * #importing the Tkinter libraries
import tkFont
from PIL import Image,ImageTk

path= 'C:\Users\mayur.sarode\Pictures\TpVision-logo.png'
root = Tk( )
img =ImageTk.PhotoImage(Image.open(path))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

root.mainloop( )
