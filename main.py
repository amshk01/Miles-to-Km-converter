import tkinter
from tkinter import *

def mile_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    result_label.config(text=f"{km}")


window = Tk()
window.title("Mile to Km")
window.config(padx=70, pady =40)

miles_input = Entry(width=5)
miles_input.grid(row=0, column=0)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=1)
is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(row=1, column=0)

result_label = Label(text="0")
result_label.grid(row=2, column=0)
km_label = Label(text="km")
km_label.grid(row=2, column=1)

calculate_button = Button(text="Calculate",command= mile_to_km)
calculate_button.grid(row=3,column=0)

window.mainloop()