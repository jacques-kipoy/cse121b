from tkinter import *
window = Tk()
window.minsize(width=500, height=300)
window.title("Miles to Kilometer")
window.config(padx=10, pady=10)

#Miles to Kilometer function
def miles_to_kilometer():
    miles = float(input.get())
    km = miles * 1.609  # the formula to convert miles to km
    label_3.config(text=f"{km}")


#Entry
input = Entry(text="0", width=7)
input.grid(column=0, row=0)

#my_widget label 0-4
label = Label(text="Miles")
label.grid(column=1, row=0)

label_2 = Label(text="is equal to")
label_2.grid(column=0, row=1)

label_3 = Label(text="0")
label_3.grid(column=0, row=3)

label_4 = Label(text="Km")
label_4.grid(column=1, row=3)

#my_button
button = Button(text="Calculate", command=miles_to_kilometer)
button.grid(column=0, row=5)





window.mainloop()
