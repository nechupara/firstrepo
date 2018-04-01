from tkinter import *
from tkinter import colorchooser
import time


def func_exit():
    pass

def not_change_hex(event):
    # entry_hex.icursor(0)
    # entry_hex.delete(0, END)
    hex_var.set(value=k[1])
    entry_hex.icursor(0)
    entry_hex.select_from(0)
    entry_hex.select_to(END)


def not_change_dec(event):
    # entry_dec.icursor(0)
    # entry_dec.delete(0, END)
    dec_var.set(value='(' + str(int(k[0][0])) + ',' + str(int(k[0][1])) +',' + str(int(k[0][2])) +')')
    entry_dec.icursor(0)
    entry_dec.select_from(0)
    entry_dec.select_to(END)


def change(event):
    # time.sleep(0.01)
    hex_var.set(value='0000000000')
    entry_hex.icursor(0)
    entry_hex.select_from(0)
    entry_hex.select_to(END)

# file_color = open('color.txt', 'w')
# file_color.write('aaaaaa')
# file_color.close()



with open('color.txt', 'r') as file_color:
    lastcolor = file_color.readline()
    print(lastcolor)

root=Tk()
root.title('Номер цвета')
root.geometry('+600+300')
root.config(bg='#369d0b')
root.resizable(width=0, height=0)
# root.protocol('WM_DELETE_WINDOW', func=func_exit)

frame_info = Frame(root, bg='#369d0b')
frame_info.grid(row=10, column=10, padx=20, pady=20)
# frame_info.grid(row=1, column=1, padx=20, pady=20, sticky= 'n')


text_dec = Label(frame_info)
text_dec.config(text='none', width=15, borderwidth=0, bg='#369d0b')
text_dec.grid(row=10, column=10, ipadx=0)

text_razdelitel_10 = Label(frame_info, width=0, bg='#369d0b', padx=0)
text_razdelitel_10.grid(row=10, column=15)

text_hex = Label(frame_info)
text_hex.config(text='none', width=15, bg='#369d0b')
text_hex.grid(row=10, column=20)


# frame_ent = Frame(root, bg='purple')
# frame_ent.place(x=20, y=70, width=260)

dec_var = StringVar()
dec_var.set(value='11111')
hex_var = StringVar()
hex_var.set(value='00000')

entry_dec = Entry(frame_info, textvariable=dec_var, justify='center', width=25)
entry_dec.grid(row = 20, column= 10)

entry_razdelitel_20 = Label(frame_info, width=0, bg='#369d0b', padx=0)
entry_razdelitel_20.grid(row=20, column=15)

entry_hex = Entry(frame_info, textvariable=hex_var, justify='center', width=25)
entry_hex.grid(row=20, column=20)

root1=Tk()
root1.geometry('+500+300')
root1.overrideredirect(1)
k = colorchooser.askcolor(parent=root1, color=lastcolor)
root1.destroy()


text_dec['text'] = '(' + str(int(k[0][0])) + ',' + str(int(k[0][1])) +',' + str(int(k[0][2])) +')'
text_hex['text'] = k[1]

dec_var.set(value='(' + str(int(k[0][0])) + ',' + str(int(k[0][1])) +',' + str(int(k[0][2])) +')')
hex_var.set(value=k[1])


entry_hex.focus_set()
entry_hex.select_to(END)

entry_hex.bind("<KeyPress>", not_change_hex)
entry_hex.bind("<KeyRelease>", not_change_hex)
entry_hex.bind("<ButtonRelease>", not_change_hex)
# entry_hex.bind("<Button-1-KeyPress>", not_change)

entry_dec.bind("<KeyPress>", not_change_dec)
entry_dec.bind("<KeyRelease>", not_change_dec)
entry_dec.bind("<ButtonRelease>", not_change_dec)

lastcolor = k[1]
with open('color.txt', 'w') as file_color:
    file_color.write(k[1])
    file_color.write('\n(' + str(int(k[0][0])) + ',' + str(int(k[0][1])) +',' + str(int(k[0][2])) +')')

root.mainloop()
print(k[0])
print(k[1])
print(round(160.6))
