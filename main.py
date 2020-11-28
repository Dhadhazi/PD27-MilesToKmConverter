from tkinter import *


def calculate(miles):
    km = round(miles*1.60934,2)
    calculated_label.config(text=km)


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=50, pady=50)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculated_label = Label(text="0")
calculated_label.grid(column=1, row=1)

input_field = Entry(width=5)
input_field.grid(column=1, row=0)

calculate_button = Button(text="Calculate", command=lambda: calculate(float(input_field.get())))
calculate_button.grid(column=1, row=3)

window.mainloop()