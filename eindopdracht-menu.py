import tkinter as tk
from datetime import datetime, timedelta

window = tk.Tk()



def show_thing_1():
    window.title("risi's gedeelte")
    frame_begin.pack_forget()
    frame_risi.pack()
    frame_gio.pack_forget()
    frame_harmen.pack_forget()
    frame_teylaa.pack_forget()

def show_thing_2():
    window.title("Gio's gedeelte")
    frame_begin.pack_forget()
    frame_gio.pack()
    frame_risi.pack_forget()
    frame_teylaa.pack_forget()
    frame_harmen.pack_forget()

def show_thing_3():
    window.title("wanneer kom je aan")
    frame_begin.pack_forget()
    frame_harmen.pack()
    frame_gio.pack_forget()
    frame_risi.pack_forget()
    frame_teylaa.pack_forget()

def show_thing_4():
    window.title("teylaa's gedeelte")
    frame_begin.pack_forget()
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


frame_begin = tk.Frame(borderwidth=10)
welkom = tk.Label(frame_begin, text="Welkom bij onze rekentool!!")
welkom.pack()

welkom2 = tk.Label(frame_begin, text="Open het menu om de functies te gebruiken")
welkom2.pack()

frame_begin.pack()
#maakt een frame voor risi
frame_risi = tk.Frame(borderwidth=10)
frame_risi.columnconfigure(index=0, weight=1)
frame_risi.columnconfigure(index=1, weight=1)

#maakt een label aan met text erin 
breedtelabel = tk.Label(frame_risi, text="Hoe breed is het vierkant?")
#zorgt ervoor dat het op de goeie positie staat
breedtelabel.grid(column=0, row=1)

#maakt een invoer veld
invoerbreedte = tk.Entry(frame_risi, width=10)
invoerbreedte.grid(column=1, row=1)

#maakt nog een label met text erin
lengtelabel = tk.Label(frame_risi, text="Hoe lang is het vierkant?")
lengtelabel.grid(column=0, row=2)

invoerlengte = tk.Entry(frame_risi, width=10)
invoerlengte.grid(column=1, row=2)

#voegt een knop aan met erop "submit"
submit = tk.Button(frame_risi, text="submit")

#zorgt ervoor dat de knop op een goeie positie is 
submit.grid(column=0, row=3)

#voegt nog een knop toe met "clear" erop
clear = tk.Button(frame_risi, text="clear")
clear.grid(column=1, row=3)

#zorgt ervoor dat er nog een text word toegevoegt op het einde
out3 = tk.Label(frame_risi, text="Wat is de omtrek en oppervlakte van uw vierkant?", width="40")
out3.grid(column=0, row=4)
out2 = tk.Label(frame_risi, text="", width="40")
out2.grid(column=0, row=5)

#zorgt ervoor dat er een stuk code word uitgevoert wanneer je om de knop submit klikt
def handle_submit(event):
    #zorgt ervoor dat de ingevoerde waarde bij de invoerveld van breede een int wordt
    breedte = int(invoerbreedte.get())
    #zorgt ervoor dat de ingevoerde waarde bij de invoerveld van lengte een int wordt
    lengte = int(invoerlengte.get())
    #maakt een som om de oppervlakte te berekenen
    oppervlakte = breedte * lengte
    #maakt een som om de omtrek te berekenen
    omtrek = (breedte + lengte) * 2 

    #maakt een zin aan met erachter de oppervlakte 
    out3["text"] ="Uw vierkant heeft een oppervlakte van " + str(oppervlakte)
    #maakt een zin aan met erachter de omtrek 
    out2["text"] = "en een omtrek van " + str(omtrek)

#zorgt ervoor dat er een stuk code word uitgevoert wanneer je om de knop clear klikt
def handle_clear(event):
    invoerbreedte.delete(0, "end")
    invoerlengte.delete(0, "end")
    out3["text"] ="Wat is de omtrek en oppervlakte van uw vierkant?"
    out2["text"] =""

clear.bind("<Button-1>", handle_clear)
submit.bind("<Button-1>", handle_submit)

#er wordt een titel aangemaakt waarin staat bereken je bmi
frame_gio = tk.Frame(borderwidth=10)
label_out = tk.Label(frame_gio, text="Bereken je BMI.", font=("Helvetica", 16))
label_out.pack(pady=20)

label = tk.Label(frame_gio, text="Voer hier je gewicht in kilo's in.", font=("Helvetica", 12))
label.pack()
#maak een invoer veld voor de andwoorden van de gebruiker
kilo = tk.Entry(master=frame_gio, width=10, font=("Helvetica", 12))
kilo.pack(pady=10)

label1 = tk.Label(frame_gio, text="voer hier je lengte in meters(bv. 1.70).", font=("Helvetica", 12))
label1.pack()

lengte = tk.Entry(master=frame_gio, width=10, font=("Helvetica", 12))
lengte.pack(pady=10)
#hier wordt andwoord de bmi weergegeven
andwoord = tk.Label(frame_gio, text="", font=("Helvetica", 12))
andwoord.pack(pady=10)
#hier wordt weergegeven als je over gewicht of normaal gewicht heb of onder gewicht
andwoord2 = tk.Label(frame_gio, text="", font=("Helvetica", 12))
andwoord2.pack(pady=10)

#button voor het verwijderen van het ingevoerde andwoorden
clear = tk.Button(master= frame_gio, text='clear')
clear.pack(pady=10)

#functie can het verwijderen van het ingevoerde andwoorden
def clear_handle(event):
    print('verwijder de input')
    kilo.delete(0, 'end')
    lengte.delete(0, 'end')

#functie voor het berekenen van de bmi en een if statement waarin staat of je een hoge, lage of normale bmi heb
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

#button voor het starten van de functie sub_handle door middel van event handeling
btn_submit = tk.Button(master=frame_gio, text="bereken", font=("Helvetica", 12), bg="green", fg="white", command=sub_handle,  )
btn_submit.pack(pady=10)

#button voor het starten van de functie clear_handle door middel van event handeling
clear.bind('<Button-1>', clear_handle)
btn_submit.bind('<Button-1>', sub_handle)

# teylaa's frame
frame_teylaa = tk.Frame(borderwidth=10)

# hier krijgt de bedrag berekening een uiterlijk
frame_teylaa.columnconfigure(index=0, weight=1)
frame_teylaa.columnconfigure(index=1, weight=1)
frame_teylaa.columnconfigure(index=2, weight=1)

# de teksten en input komt erbij. met de input kan het de btw berekenen
bedraglabel = tk.Label(frame_teylaa, text="Wat is uw bedrag?") 
bedraglabel.grid(column=0, row=1)

invoerbedrag = tk.Entry(frame_teylaa, width=10)
invoerbedrag.grid(column=1, row=1)

BTWLabel = tk.Label(frame_teylaa, text="wat is het BTW van uw bedrag (21/9)")
BTWLabel.grid(column=0, row=2)

invoerBTW = tk.Entry(frame_teylaa, width=10)
invoerBTW.grid(column=1, row=2)

submit = tk.Button(frame_teylaa, text="submit")
submit.grid(column=0, row=3)

clear = tk.Button(frame_teylaa, text="clear")
clear.grid(column=1, row=3)

out4 = tk.Label(frame_teylaa, text="Wat is uw bedrag na het BTW ", width="40")
out4.grid(column=0, row=4)

# dit is de code waar de user input word berekent met de gekozen btw.
def handle_submit(event):
    bedrag = int(invoerbedrag.get())
    BTW = int(invoerBTW.get())
    eindbedrag = bedrag / 100 * (100 + BTW)
    out4["text"] ="uw eindbedrag is " , eindbedrag , 'euro' 

def handle_clear(event):
    invoerbedrag.delete(0, "end")
    invoerBTW.delete(0, "end")
    out4["text"] ="Wat us uw bedrag na het BTW?"


# dit herstart de programma. 
clear.bind("<Button-1>", handle_clear)
submit.bind("<Button-1>", handle_submit)


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