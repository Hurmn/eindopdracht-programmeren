import tkinter as tk

window = tk.Tk()
window.title("Welkom bij ontspanningstool")


label_out = tk.Label(window, text="Bereken je BMI.", font=("Helvetica", 16))
label_out.pack(pady=20)

label = tk.Label(window, text="Voer hier je gewicht in kilo's in.", font=("Helvetica", 12))
label.pack()

kilo = tk.Entry(master=window, width=10, font=("Helvetica", 12))
kilo.pack(pady=10)

label1 = tk.Label(window, text="voer hier je lengte in meters(bv. 1,70).", font=("Helvetica", 12))
label1.pack()

lengte = tk.Entry(master=window, width=10, font=("Helvetica", 12))
lengte.pack(pady=10)

andwoord = tk.Label(window, text="", font=("Helvetica", 12))
andwoord.pack(pady=10)


clear = tk.Button(master= window, text='clear')
clear.pack(pady=10)

image = tk.PhotoImage(file="bmi.png")
label3 = tk.Label(window, image=image)
label3.pack()

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

btn_submit = tk.Button(master=window, text="bereken", font=("Helvetica", 12), bg="green", fg="white", command=sub_handle)
btn_submit.pack(pady=10)

clear.bind('<Button-1>', clear_handle)
btn_submit.bind('<Button-1>', sub_handle)

window.configure(bg="white")  # achtergrondkleur van het venster
window.mainloop()