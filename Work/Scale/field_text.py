from tkinter import *

def text_edit():
    text1.insert('3.2', 'aaaa')
    # text1.delete(2.1,END)

root = Tk()
root.title('Text')
root.geometry('+600+300')


text1=Text()
text1.insert(1.1, 'bbbbbbb\nbbbbbbb\nbbbbbbb\nbbbbbbb\nbbbbbbb\nbbbbbbb\nbbbbbbb\nbbbbbbb\nbbbbbbb\nbbbbbbb\n')
text1.pack()

button = Button(root, text='click me', command=text_edit)
button.pack()

root.mainloop()