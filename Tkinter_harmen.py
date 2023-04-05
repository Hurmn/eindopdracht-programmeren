import tkinter as tk
from datetime import datetime, timedelta

window = tk.Tk()
window.title("Wanneer kom je aan")

window.columnconfigure(index=0, weight=1)
window.columnconfigure(index=1, weight=1)
window.columnconfigure(index=2, weight=1)

afstandlabel = tk.Label(window, text="Hoeveel kilometer?")
afstandlabel.grid(column=0, row=1)

invoerAfstand = tk.Entry(window, width=10)
invoerAfstand.grid(column=1, row=1)

snelheidLabel = tk.Label(window, text="Wat is je snelheid(Km/u)")
snelheidLabel.grid(column=0, row=2)

invoerSnelheid = tk.Entry(window, width=10)
invoerSnelheid.grid(column=1, row=2)

submit = tk.Button(window, text="submit")
submit.grid(column=0, row=3)

clear = tk.Button(window, text="clear")
clear.grid(column=1, row=3)

out = tk.Label(window, text="Hoelang duurt je reis", width="40")
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