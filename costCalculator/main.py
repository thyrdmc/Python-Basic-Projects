# TODO 3: Store Data by Creating a DataFrame and CSV File
from tkinter import *
import pandas


def calculate():
    dataset = pandas.read_csv("data.csv")
    text = f"{round(sum(dataset.total) / sum(dataset.amount), 2)}" if sum(dataset.amount) != 0 else 0
    print(sum(dataset.amount))
    print(sum(dataset.total))
    return text


# TODO 1: Create Window and Configurate GUI

screen = Tk()

screen.title("Cost Calculator")
screen.minsize(width=250, height=200)
screen.config(padx=30, pady=30)

lbl_lot = Label(text='Lot')
lbl_lot.grid(row=0, column=2)

lbl_price = Label(text='Price')
lbl_price.grid(row=1, column=2)

lbl = Label(text='is equal to')
lbl.grid(row=2, column=0)

lbl_cost = Label(text='Cost')
lbl_cost.grid(row=2, column=2)

final_cost = Label(text=calculate())
final_cost.grid(row=2, column=1)

textbox_price = Entry(width=7)
textbox_price.grid(row=1, column=1)

txt_lot = Entry(width=7)
txt_lot.grid(row=0, column=1)


# TODO 2: Create the Required Functionality.
def button_clicked():
    lot = float(txt_lot.get())
    price = float(textbox_price.get())
    data_dict = {"price": [price], "amount": [float(lot)], "total": [price * lot]}
    df = pandas.DataFrame(data_dict)
    df.to_csv("data.csv", mode="a", index=False, header=False)

    final_cost.config(text=calculate())


button = Button(text="Calculate", command=button_clicked)
button.grid(row=3, column=1)

screen.mainloop()
