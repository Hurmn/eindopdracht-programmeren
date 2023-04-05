import tkinter as tk
from datetime import datetime, timedelta

window = tk.Tk()



def show_thing_1():
    window.title("risi's gedeelte")
    frame_risi.pack()
    frame_gio.pack_forget()
    frame_harmen.pack_forget()
    frame_teylaa.pack_forget()

def show_thing_2():
    window.title("Gio's gedeelte")
    frame_gio.pack()
    frame_risi.pack_forget()
    frame_teylaa.pack_forget()
    frame_harmen.pack_forget()

def show_thing_3():
    window.title("wanneer kom je aan")
    frame_harmen.pack()
    frame_gio.pack_forget()
    frame_risi.pack_forget()
    frame_teylaa.pack_forget()

def show_thing_4():
    window.title("teylaa's gedeelte")
    frame_teylaa.pack()
    frame_harmen.pack_forget()
    frame_gio.pack_forget()
    frame_risi.pack_forget()

window.title("De-RechteBanaan")

menubar = tk.Menu(window)
window.config(menu=menubar)


mainmenu = tk.Menu(menubar)
mainmenu.add_command(label="Risi's gedeelte", command=show_thing_1)
mainmenu.add_command(label="Gio's gedeelte", command=show_thing_2)
mainmenu.add_command(label="Wanneer kom je aan", command=show_thing_3)
mainmenu.add_command(label="Teylaa's gedeelte", command=show_thing_4)
mainmenu.add_separator
mainmenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="Tool", menu=mainmenu)

frame_risi = tk.Frame(borderwidth=10)
label_1 = tk.Label(frame_risi, text="Risi's gedeelte", bg = "blue", fg="white", width=20, height=8)
label_1.pack()

frame_gio = tk.Frame(borderwidth=10)
label_2 = tk.Label(frame_gio, text="gedeelte gio", bg = "red", fg="white", width=20, height=8)
label_2.pack()

frame_teylaa = tk.Frame(borderwidth=10)
label_3 = tk.Label(frame_teylaa, text="Teylaa's gedeelte", bg = "green", fg="white", width=20, height=8)
label_3.pack()


#Harmens gedeelte
frame_harmen = tk.Frame(borderwidth=10)

#Grid maken
window.columnconfigure(index=0, weight=1)
window.columnconfigure(index=1, weight=1)

#afstand bepalen
afstandlabel = tk.Label(frame_harmen, text="Hoeveel kilometer?")
afstandlabel.grid(column=0, row=1)
invoerAfstand = tk.Entry(frame_harmen, width=10)
invoerAfstand.grid(column=1, row=1)

#snelheid bepalen
snelheidLabel = tk.Label(frame_harmen, text="Wat is je snelheid(Km/u)")
snelheidLabel.grid(column=0, row=2)
invoerSnelheid = tk.Entry(frame_harmen, width=10)
invoerSnelheid.grid(column=1, row=2)

#submit en clear knoppen
submit = tk.Button(frame_harmen, text="submit")
submit.grid(column=0, row=3)
clear = tk.Button(frame_harmen, text="clear")
clear.grid(column=1, row=3)

#output
out = tk.Label(frame_harmen, text="Hoelang duurt je reis", width="40")
out.grid(column=0, row=4)

def handle_submit(event):
    #bepaal de tijd
    nu = datetime.now()
    #afstand en tijd in variabele gezet
    afstand = int(invoerAfstand.get())
    snelheid = int(invoerSnelheid.get())
    #reistijd bepalen
    minuten = afstand / snelheid * 60
    #tijdsverschil bepalen om aankomstijd uit te kunnen rekenen
    tijdVerschil = timedelta(minutes= minuten)
    aankomstTijd = nu + tijdVerschil
    #output neerzetten
    out["text"] ="de reis duurt " + str(minuten) + "minuten en je komt aan om " + aankomstTijd.strftime("%H:%M")

def handle_clear(event):
    invoerAfstand.delete(0, "end")
    invoerSnelheid.delete(0, "end")
    out["text"] ="Hoelang duurt je reis"

clear.bind("<Button-1>", handle_clear)
submit.bind("<Button-1>", handle_submit)

window.mainloop()