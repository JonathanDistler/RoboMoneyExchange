import requests
import tkinter as tk
from tkinter import messagebox

#all in form of x-stockabrev-zusd
eth="XETHZUSD"
ltc="XLTCZUSD"
bitcoin="XXBTZUSD"


#link doesn't work for doge, check on website
doge="XXDGZUSD"

stock_symbols=["XETHZUSD","XLTCZUSD","XXBTZUSD"]

#returns the current price of one stock in USD, uses an API call to kraken website-Yahoo Finance didn't let me call JSon
def get_crypto_price(kraken_call):
    url=f"https://api.kraken.com/0/public/Ticker?pair={kraken_call}"
    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        price = float(data["result"][kraken_call]["c"][0])  # 'c' is the last trade closed price
        #need to work on the string and strip betweeen the last X and USD
        x_index=kraken_call.rfind("X")
        U_index=kraken_call.rfind("U")
        str_update=kraken_call[x_index+1:U_index]
        messagebox.showinfo("Price", f"{str_update} price is ${price:.2f} USD")
        return price
    except Exception as e:
        print(f"Error fetching BTC price from Kraken: {e}")
        return None

#gets cost of specific stock
#name=ltc
#crypto_price = get_crypto_price(name)

#gets the number of stocks for certin cryptocurrency based on user inputted 
def crypto_stock_num(USD,crypto_rate):
    return(USD/crypto_rate)

#example call 
#num_stocks=crypto_stock_num(50,crypto_price)


root = tk.Tk()
root.title("Simple Stock Price")

for stock in stock_symbols:
    btn = tk.Button(root, text=stock, width=15, command=lambda s=stock: get_crypto_price(s))
    btn.pack(padx=10, pady=5)

root.mainloop()
