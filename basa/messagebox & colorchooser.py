from tkinter import *
from tkinter import colorchooser #импорт функции colorchooser обязателен отдельно
color = colorchooser.askcolor()
print(color)
###################
from tkinter import *
from tkinter import messagebox #импорт функции messagebox обязателен отдельно
root = Tk()
root.title("GUI на Python")
root.geometry("300x250")
messagebox.showinfo("GUI Python", 'example message')
"""
message = StringVar()
messagebox.showinfo("GUI Python",  message.get())
"""
root.mainloop()