def interpolation(x0, y0, x1, y1, x):
    y = y0 + (y1 - y0) / (x1 - x0) * (x - x0)
    return y



x0 = 12.11
y0 = 325

x = 10
# y =

x1 = 11.74
y1 = 320


# y = y0 + (y1 - y0)/(x1 - x0)*(x - x0)
print(y0 + (y1 - y0)/(x1 - x0)*(x - x0))

#Графическое окно:
root = tk.Tk()
root.title('Интерполяция')
screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()
root_height = root.winfo_height()
root_width = root.winfo_width()
root_x = screen_width/2 - root_width/2
root_y = screen_height/2 - root_height/2
root.geometry('+%d+%d' % (root_x, root_y))

#Главная рамка:
frame_root = Frame()
frame_root.pack()
#Рамка для ввода данных:
frame_input = Frame(frame_root)
frame_input.grid()

#строка с надписями и полями для ввода для значений X
label_x1 = Label(frame_input, text='x1')
label_x1.grid(row=10, column=10)

enter_x1 = Entry(frame_input)
enter_x1.grid(row=10, column=20)





root.mainloop()