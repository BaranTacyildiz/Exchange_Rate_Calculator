import tkinter as tk
from tkinter import ttk
import requests



def ExchangeCalculator():
    Currency = CurrencyData.get() # We chose the currency we have
    CurrenctToChange = CurrencyToChangeData.get() # We selected the currency to change
    Amount = float(DataOfAmount.get()) # We got the amount of currency we have
    url = f"https://api.exchangerate-api.com/v4/latest/{Currency}" # We entered the URL to learn the value of the currency from the API.
    response = requests.get(url) # We got data from API url.
    data = response.json() # We converted the data to json format.
    ExchangeRate = data['rates'][CurrenctToChange]
    AmountOfCurrenyToChange = Amount * ExchangeRate # Here we calculated the result
    ResultLabel.config(text=f"{Amount} {Currency} = {AmountOfCurrenyToChange} {CurrenctToChange}") # And we printed it on screen.

root = tk.Tk()
root.title("Exchange Rate Calculator")

CurrencyLabel = ttk.Label(root, text="Select the currency you have: ")
CurrencyLabel.pack()

CurrencyData = ttk.Combobox(root, values=["USD", "EUR", "GBP","TRY"])
CurrencyData.pack()

AmountLabel = ttk.Label(root, text="Enter your money amount:")
AmountLabel.pack()

DataOfAmount = ttk.Entry(root)
DataOfAmount.pack()

CurrencyToChangeLabel = ttk.Label(root, text="Select the currency you want to change your money to:")
CurrencyToChangeLabel.pack()

CurrencyToChangeData = ttk.Combobox(root, values=["USD", "EUR", "GBP","TRY"])
CurrencyToChangeData.pack()

ResultButton = ttk.Button(root, text="Calculate the Exchange Rate", command=ExchangeCalculator)
ResultButton.pack()

ResultLabel = ttk.Label(root, text="")
ResultLabel.pack()

root.mainloop()
