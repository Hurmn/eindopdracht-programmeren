import tkinter as tk

window = tk.Tk()
window.title("Welkom bij ontspanningstool")

label_out = tk.Label(window, text="Bereken je BMI.", font=("Helvetica", 16))
label_out.pack(pady=20)

label_weight = tk.Label(window, text="Voer hier je gewicht in kilo's in.", font=("Helvetica", 12))
label_weight.pack()

weight_entry = tk.Entry(master=window, width=10, font=("Helvetica", 12))
weight_entry.pack(pady=10)

label_height = tk.Label(window, text="Voer hier je lengte in meters(bv. 1.70).", font=("Helvetica", 12))
label_height.pack()

height_entry = tk.Entry(master=window, width=10, font=("Helvetica", 12))
height_entry.pack(pady=10)

result_label = tk.Label(window, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    bmi = weight / (height ** 2)
    result_label.config(text="Je BMI is {:.1f}".format(bmi))

btn_submit = tk.Button(master=window, text="Bereken", font=("Helvetica", 12), bg="green", fg="white", command=calculate_bmi)
btn_submit.pack(pady=10)

clear_btn = tk.Button(master=window, text='Clear', font=("Helvetica", 12), command=lambda: (weight_entry.delete(0, 'end'), height_entry.delete(0, 'end'), result_label.config(text="")))
clear_btn.pack(pady=10)

window.configure(bg="white")
window.mainloop()