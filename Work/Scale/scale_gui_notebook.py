from tkinter import *
from tkinter import ttk

class Label_1(Label):
    def __init__(self, master):
        Label.__init__(self, master)
        self.config(bg='#ffeaf4')

class Entry_1(Entry):
    def __init__(self, master):
        Entry.__init__(self,  master)
        self.config(bg='#b9b9dd')

class Frame_1(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        

class Frame_1(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

class Text_1(Text):
    def __init__(self, master):
        Text.__init__(self, master)
        self.config(bg='yellow')


class Button_1(Button):
    def __init__(self, master):
        Button.__init__(self, master)
        self.configure(bg='purple')

def enter(event):
    text_output.configure(state='normal')
    text_output.delete(1.0, END)
    text_output.insert(1.0, 'ENTER')
    text_output.configure(state='disabled')


def calculation():
    scale1 = float(entry_scale1.get())
    print(scale1)
    scale2 = float(entry_scale2.get())
    print(scale2, end='\n\n')
    mm_to_m = scale2 / (scale1 * 1000)
    m_to_mm = scale1 * 1000 / scale2

    mm_to_km = mm_to_m / 1000
    km_to_mm = m_to_mm * 1000

    text_output.configure(state='normal')
    text_output.delete(1.0, END)

    text_output.insert(1.0, 'масштаб %s:%s' % (int(scale1), int(scale2)) + '\n\n')

    text_output.insert(3.0, 'в 1 мм %s м\t\t(/%s)\n' % (mm_to_m, m_to_mm))
    text_output.insert(4.0, 'в 1 м  %s мм\t\t(/%s)\n\n' % (m_to_mm, mm_to_m))
    text_output.insert(6.0, 'в 1 мм %s км\t\t(/%s)\n' % (mm_to_km, km_to_mm))
    text_output.insert(7.0, 'в 1 км %s мм\t\t(/%s)\n' % (km_to_mm, mm_to_km))

    text_output.configure(state='disabled')

    # text_out_01_res['text'] = str(mm_to_m)
    # text_out_11_res['text'] = str(m_to_mm)





root = Tk()
root.title('Масштаб')
root.geometry('+600+300')
root.tk_setPalette(background='#55ffaa')

notebook = ttk.Notebook(root)
notebook.grid(row=0, column=0)
######frame root
##
frame_root = Frame_1(root)
frame_root.grid(row=0, column=0, padx=20, pady=20)

##
#############

######frame input (ввод)
##
frame_input = Frame_1(frame_root)
frame_input.grid(row=10, column=10)

label_in_scale=Label_1(frame_input)
label_in_scale.config(text="Масштаб")
label_in_scale.grid(row=10, column=10)

label_razd0 = Label_1(frame_input)
label_razd0.grid(row=10, column=15, padx=5)

entry_scale1 = Entry_1(frame_input)
entry_scale1.config(width=6, justify='c')
entry_scale1.insert(0,1)
entry_scale1.grid(row=10, column=20)

label_razd1 = Label_1(frame_input)
label_razd1.configure(text=':')
label_razd1.grid(row=10, column=25)

entry_scale2 = Entry_1(frame_input)
entry_scale2.config(width=8, justify=CENTER)
entry_scale2.insert(0,500)
entry_scale2.grid(row=10, column=30)
##
###############


#######frame output (Вывод)
##
frame_output = Frame_1(frame_root)
frame_output.configure(pady=20)
frame_output.grid(row=20, column=10, sticky=W)

text_output = Text_1(frame_output)
text_output.configure(state='disabled')
text_output.configure(height=8)
text_output.pack()
##
###########################################



#########frame buttons (кнопки)
##
frame_button = Frame_1(frame_root)
frame_button.grid(row=30, column=10)

button_do = Button_1(frame_button)
button_do.configure(text='Рассчитать', command=calculation)
button_do.grid(row=10, column=10)
##
#################################


# entry_scale1.bind('<KeyRelease>', input_scale)
# root.bind('<KeyPress-Return>', enter)
# entry_scale2.unbind('<KeyPress-Return>')
# button_do.bind('<KeyPress-Return>', enter)

###Notebook

notebook.add(frame_root, text='1')



root.mainloop()