from tkinter import *

window = Tk()
window.title("My GUI program")
window.minsize(width=500,height=300) 
window.config(padx=10, pady=10)




#Label

my_label = Label(text="I am a label", font=("Arial",24, "bold"))
#my_label.pack()
my_label.grid(column=0, row=0)
#Button

def button_clicked():
    print("I got click")
    my_label.config(text=input.get())
    print(input.get())

button = Button(text="Click Me", command=button_clicked)
#button.pack()
button.grid(column=2, row=2)

button_2 = Button(text="Hello")
button_2.grid(column=3, row=1)

#Entry 

input = Entry(width=10)
#input.pack()
input.grid(column=4, row=4)
input.get()


window.mainloop()

