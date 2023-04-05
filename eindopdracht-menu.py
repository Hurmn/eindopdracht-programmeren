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
frame_risi.columnconfigure(index=0, weight=1)
frame_risi.columnconfigure(index=1, weight=1)

breedtelabel = tk.Label(frame_risi, text="Hoe breed is de vierkant?")
breedtelabel.grid(column=0, row=1)

invoerbreedte = tk.Entry(frame_risi, width=10)
invoerbreedte.grid(column=1, row=1)

lengtelabel = tk.Label(frame_risi, text="Hoe lengte is de vierkant?")
lengtelabel.grid(column=0, row=2)

invoerlengte = tk.Entry(frame_risi, width=10)
invoerlengte.grid(column=1, row=2)

submit = tk.Button(frame_risi, text="submit")
submit.grid(column=0, row=3)

clear = tk.Button(frame_risi, text="clear")
clear.grid(column=1, row=3)

out3 = tk.Label(frame_risi, text="Wat is de omtrek en oppervlakte van uw vierkant?", width="40")
out3.grid(column=0, row=4)
out2 = tk.Label(frame_risi, text="", width="40")
out2.grid(column=0, row=5)

def handle_submit(event):
    breedte = int(invoerbreedte.get())
    lengte = int(invoerlengte.get())
    oppervlakte = breedte * lengte
    omtrek = (breedte + lengte) * 2 
    out3["text"] ="Uw vierkant heeft een oppervlakte van " + str(oppervlakte)
    out2["text"] = "en een omtrek van " + str(omtrek)


def handle_clear(event):
    invoerbreedte.delete(0, "end")
    invoerlengte.delete(0, "end")
    out3["text"] ="Wat is de omtrek en oppervlakte van uw vierkant?"
    out2["text"] =""

clear.bind("<Button-1>", handle_clear)
submit.bind("<Button-1>", handle_submit)


frame_gio = tk.Frame(borderwidth=10)
label_out = tk.Label(frame_gio, text="Bereken je BMI.", font=("Helvetica", 16))
label_out.pack(pady=20)

label = tk.Label(frame_gio, text="Voer hier je gewicht in kilo's in.", font=("Helvetica", 12))
label.pack()

kilo = tk.Entry(master=frame_gio, width=10, font=("Helvetica", 12))
kilo.pack(pady=10)

label1 = tk.Label(frame_gio, text="voer hier je lengte in meters(bv. 1.70).", font=("Helvetica", 12))
label1.pack()

lengte = tk.Entry(master=frame_gio, width=10, font=("Helvetica", 12))
lengte.pack(pady=10)

andwoord = tk.Label(frame_gio, text="", font=("Helvetica", 12))
andwoord.pack(pady=10)

andwoord2 = tk.Label(frame_gio, text="", font=("Helvetica", 12))
andwoord2.pack(pady=10)


clear = tk.Button(master= frame_gio, text='clear')
clear.pack(pady=10)


def clear_handle(event):
    print('verwijder de input')
    kilo.delete(0, 'end')
    lengte.delete(0, 'end')

def sub_handle(event):
    print('knop gedrukt')
    lengte2 = float(lengte.get())
    kilo2 = float(kilo.get())
    bmi = kilo2/ (lengte2 ** 2)
    andwoord.config(text="Je BMI is {:.1f}".format(bmi))
    if bmi <= 18.5:
        andwoord2["text"] ="je heb ondergewicht"
    elif bmi > 25:
        andwoord2["text"] ="je heb overgewicht"
    else:
        andwoord2["text"] ="je heb een normaal gewicht"


btn_submit = tk.Button(master=frame_gio, text="bereken", font=("Helvetica", 12), bg="green", fg="white", command=sub_handle,  )
btn_submit.pack(pady=10)

clear.bind('<Button-1>', clear_handle)
btn_submit.bind('<Button-1>', sub_handle)

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