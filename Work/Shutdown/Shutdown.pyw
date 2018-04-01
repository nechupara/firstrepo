import os
import tkinter as tk
from tkinter.ttk import *

digits = ['0','1','2','3','4','5','6','7','8','9']

def shutdown():
    flag = True
    minits = input_min.get()
    for i in minits:
        if i not in digits:
            flag = False
    if flag and len(minits) != 0 and int(minits) < 5000000 and int(minits) != 0: #315360000
        os.system('shutdown.exe /s /t %s' % (int(minits)*60))
        print('норм число, ёпта')
        
    else:
        print('гавно число')
        
def abort():
    os.system('shutdown.exe /a')

y = 700
# os.system('shutdown /s /t %s' % (y))

root = tk.Tk()
root.title('Выключение компьютера')
screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()
# root_height = root.winfo_height()
# root_width = root.winfo_width()
root_width = 500
root_height = 300
root_x = screen_width/2 - root_width/2
root_y = screen_height/2 - root_height/2
root.geometry('%dx%d+%d+%d' % (root_width, root_height, root_x, root_y))


style = Style()
style.configure('OFF.TButton', font='20')


frame_root = Frame()
frame_root.pack()
#Рамка для ввода данных:
frame_input = Frame(frame_root)
frame_input.pack()

label_input = Label(frame_input, text='Время до выключения')
label_input.grid(row='10', column='10', padx='15', pady='15')

input_min = Entry(frame_input)
input_min.grid(row='10', column='20')

label_min = Label(frame_input, text='минут')
label_min.grid(row='10', column='300')

frame_button = Frame(frame_root)
frame_button.pack()

button_off = Button(frame_button, text='Выключить', command=shutdown, style='OFF.TButton')
button_off.grid(row='10')

button_abort = Button(frame_button, text='Отменить выключение', command=abort)
button_abort.grid(row='20')

print('ширина = ' + str(root_width))
print('высота = ' + str(root_height))

root.mainloop()