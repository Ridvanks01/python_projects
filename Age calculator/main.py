import tkinter as tk
from tkinter import *
from datetime import date

root = Tk()
root.geometry("800x600")
root.resizable(False, False)
root.title("Age Calculator")



photo = PhotoImage(file= "photo.png")
myImage = Label(image=photo)
myImage.pack(padx=15, pady=15)

root.mainloop()