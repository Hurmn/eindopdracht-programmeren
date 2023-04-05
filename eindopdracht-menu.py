import tkinter as tk
from datetime import datetime, timedelta

window = tk.Tk()



def show_thing_1():
    frame_thing_2.pack_forget()
    frame_harmen.pack_forget()
    frame_thing_1.pack()

def show_thing_2():
    frame_thing_2.pack()
    frame_thing_1.pack_forget()
    frame_harmen.pack_forget()

def show_thing_3():
    window.title("wanneer kom je aan")
    frame_harmen.pack()
    frame_thing_1.pack_forget()
    frame_thing_2.pack_forget()

window.title("Menu voorbeeld")

menubar = tk.Menu(window)
window.config(menu=menubar)


mainmenu = tk.Menu(menubar)
mainmenu.add_command(label="Risi's spelletje", command=show_thing_1)
mainmenu.add_command(label="teylaa's spelletje", command=show_thing_2)
mainmenu.add_command(label="Wanneer kom je aan", command=show_thing_3)
mainmenu.add_separator
mainmenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="Tool", menu=mainmenu)

frame_thing_1 = tk.Frame(borderwidth=10)
label_1 = tk.Label(frame_thing_1, text="Risi's game", bg = "blue", fg="white", width=20, height=8)
label_1.pack()

frame_thing_2 = tk.Frame(borderwidth=10)
label_2 = tk.Label(frame_thing_2, text="teylaa's game", bg = "red", fg="white", width=20, height=8)
label_2.pack()

frame_harmen = tk.Frame(borderwidth=10)

window.columnconfigure(index=0, weight=1)
window.columnconfigure(index=1, weight=1)
window.columnconfigure(index=2, weight=1)

afstandlabel = tk.Label(frame_harmen, text="Hoeveel kilometer?")
afstandlabel.grid(column=0, row=1)

invoerAfstand = tk.Entry(frame_harmen, width=10)
invoerAfstand.grid(column=1, row=1)

snelheidLabel = tk.Label(frame_harmen, text="Wat is je snelheid(Km/u)")
snelheidLabel.grid(column=0, row=2)

invoerSnelheid = tk.Entry(frame_harmen, width=10)
invoerSnelheid.grid(column=1, row=2)

submit = tk.Button(frame_harmen, text="submit")
submit.grid(column=0, row=3)

clear = tk.Button(frame_harmen, text="clear")
clear.grid(column=1, row=3)

out = tk.Label(frame_harmen, text="Hoelang duurt je reis", width="40")
out.grid(column=0, row=4)

def handle_submit(event):
    nu = datetime.now()
    afstand = int(invoerAfstand.get())
    snelheid = int(invoerSnelheid.get())
    minuten = afstand / snelheid * 60
    tijdVerschil = timedelta(minutes= minuten)
    aankomstTijd = nu + tijdVerschil
    out["text"] ="de reis duurt " + str(minuten) + "minuten en je komt aan om " + aankomstTijd.strftime("%H:%M")

def handle_clear(event):
    invoerAfstand.delete(0, "end")
    invoerSnelheid.delete(0, "end")
    out["text"] ="Hoelang duurt je reis"

clear.bind("<Button-1>", handle_clear)
submit.bind("<Button-1>", handle_submit)

window.mainloop()