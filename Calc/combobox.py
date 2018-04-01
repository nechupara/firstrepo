from tkinter import *
from tkinter import ttk
def open_frame():
    combo.place(x=0, y=0)


def close_frame():
    combo.place_forget()

root = Tk()
root.title('combobox')
root.geometry('600x400+350+200')
frame1 = ttk.Frame(root, width=300)

frame1.place(x = 100, y = 100, height=100)
combo = ttk.Combobox(frame1, values=(1,3,5))
combo.current(1)
# combo.place(x =0, y = 0)
btn_close = Button(root, text='Close', command=close_frame)
btn_close.place(x = 10, y = 10)
btn_open = Button(root, text='Open', command=open_frame)
btn_open.place(x = 100, y = 10)

print(frame1.winfo_class())
root.mainloop()