from tkinter import *

window = Tk()
window.title("Menu voorbeeld")


def show_thing_1():
    frame_thing_2.pack_forget()
    frame_thing_1.pack()

def show_thing_2():
    frame_thing_2.pack()
    frame_thing_1.pack_forget()


menubar = Menu(window)
window.config(menu=menubar)


mainmenu = Menu(menubar)
mainmenu.add_command(label="Risi's spelletje", command=show_thing_1)
mainmenu.add_command(label="teylaa's spelletje", command=show_thing_2)
mainmenu.add_separator
mainmenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="Tool", menu=mainmenu)

frame_thing_1 = Frame(borderwidth=10)
label_1 = Label(frame_thing_1, text="Risi's game", bg = "blue", fg="white", width=20, height=8)
label_1.pack()

frame_thing_2 = Frame(borderwidth=10)
label_2 = Label(frame_thing_2, text="teylaa's game", bg = "red", fg="white", width=20, height=8)
label_2.pack()

window.mainloop()