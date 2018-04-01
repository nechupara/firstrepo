
# Craig Hammond 2016
from tkinter import *
from tkinter import ttk
class Application(Frame):
   """A GUI application """
   def __init__(self, master):
     """ Initialize the Frame"""
     ttk.Frame.__init__(self, master)
     self.grid()
     self.create_widgets()
   def create_widgets(self):
     """ create the window layout. """
     myFont = ('Lucida Grande', 12)
     #create Label Symbol
     self.label2 = Label(self, font=myFont, text="Symbol").grid(row=0, column=0)
     # create combobox for the symbol
     self.cbSymbol = ttk.Combobox(self, font=myFont, width=7, textvariable = varSymbol)
     self.cbSymbol.bind("<Return>", self.cbSymbol_onEnter) #when the enter key is press an event happens
     self.cbSymbol.bind('<<ComboboxSelected>>',self.cbSymbol_onEnter)
     self.cbSymbol['values'] = ('AAPL','FB','NFLX')
     self.cbSymbol.grid(row=0, column =1,sticky = W)
   def cbSymbol_onEnter(self, event):
     # changes characters to upper case
     varSymbol.set(varSymbol.get().upper())
     # gets the value of the text in the combobox. cbSymbol
     mytext = varSymbol.get()
     # gets list of values from dropdwn list of
     # cbSymbol combobox
     vals = self.cbSymbol.cget('values')
     # selects all in the combobox. cbSymbol
     self.cbSymbol.select_range(0, END)
     print(mytext)
     # checks if symbol exists in the combobox if not it adds it
     # to the dropdown list
     if not vals:
       self.cbSymbol.configure(values = (mytext, ))
     elif mytext not in vals:
       self.cbSymbol.configure(values = vals + (mytext, ))
     return 'break'
root = Tk()
root.title("Combobox")
root.geometry("600x480")
varSymbol = StringVar(root, value='NFLX')
app = Application(root)
root.mainloop()

###########################################

# from tkinter import *
#
# def onclick():
#    pass
#
# root = Tk()
# text = Text(root)
# text.insert(INSERT, "Hello.....")
# text.insert(END, "Bye Bye.....")
# text.pack()
#
# text.tag_add("here", "1.0", "1.4")
# text.tag_add("start", "1.8", "1.13")
# text.tag_config("here", background="yellow", foreground="blue")
# text.tag_config("start", background="black", foreground="green")
# root.mainloop()


##################################################

