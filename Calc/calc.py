import tkinter
def new_page(event=None):
    num_page = int(event.widget.curselection()[0]+1)
    labl["text"] = labl["text"][:-1] + str(num_page)
root = tkinter.Tk()
listb = tkinter.Listbox(root, height=5)
listb.insert("end", *[i for i in range(1, 6)])
listb.pack(side="left")
listb.bind("<ButtonRelease-1>", new_page)
labl = tkinter.Label(root, text="Text or lines for page 1")
labl.pack(side="right")
root.mainloop()