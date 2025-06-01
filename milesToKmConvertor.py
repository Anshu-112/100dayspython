from tkinter import *


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20, bg="#f0f4f8")

# Function to convert miles to kilometers
def miles_to_Km():
        miles = float(miles_input.get())
        km = round(miles * 1.609, 2)
        result_label.config(text=f"{km}")



title_label = Label(text="🌍 Miles to Kilometers", font=("Segoe UI", 14, "bold"), fg="#007bff", bg="#f0f4f8")
title_label.grid(column=0, row=0, columnspan=3, pady=(0, 20))

miles_input = Entry(width=10, font=("Segoe UI", 12))
miles_input.grid(column=1, row=1)

miles_label = Label(text="Miles", font=("Segoe UI", 11), bg="#f0f4f8", fg="#333333")
miles_label.grid(column=2, row=1)

is_equal_label = Label(text="is equal to", font=("Segoe UI", 11), bg="#f0f4f8", fg="#333333")
is_equal_label.grid(column=0, row=2)

result_label = Label(text="0", font=("Segoe UI", 11, "bold"), bg="#f0f4f8", fg="#28a745")
result_label.grid(column=1, row=2)

km_label = Label(text="Km", font=("Segoe UI", 11), bg="#f0f4f8", fg="#333333")
km_label.grid(column=2, row=2)


calculate_button = Button(
    text="🚀 Convert",bg="#007bff",
    activebackground="#0056b3",
    command=miles_to_Km
)
calculate_button.grid(column=1, row=3, pady=20)

window.mainloop()
