from tkinter import *

class ButtonA(Button):
    def __init__(self,master):
        Button.__init__(self,master, text='Knopka')
        # self.configure(justify='left', bg='gray', width=50)

root = Tk()
root.title('Расчёт 2/3 стрелы провиса')
root.geometry('500x400+300+200')

labl_op_A = Label(root, text = 'Высота опоры А', justify='right', bg = 'gray')
labl_op_A.grid(column = 5, row = 5)

op_A_var = StringVar(value=56)
ent_op_A = Entry(textvariable=op_A_var, width= 5, justify='center')
ent_op_A.grid(column = 6, row = 5)

btn_op_A = ButtonA(root) #Button(text = 'Click', width = '5', font='Arial 9')
# btn_op_A['text']='Click'
btn_op_A.grid(column = 0, row = 0)


root.mainloop()