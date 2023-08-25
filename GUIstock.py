from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import datetime
from tkinter import *
from tkinter import ttk,messagebox

date = datetime.now().strftime("%d-%b-%Y")
root = Tk()
root.title(f"ราคาหุ้น{date}")
root.geometry("500x400+800+100")

bg = PhotoImage(file=r"C:\Users\User\Desktop\Learning\PythonGUI\web scraping\stock.png")
BG = Label(root,image=bg)
BG.pack()

L1 = Label(root,text="ป้อนชื่อหุ้นที่ต้องการทราบราคา",font=20)
L1.pack()


textSymbol = StringVar()
E1 = ttk.Entry(root,textvariable=textSymbol,font=20)
E1.pack()
E1.focus()


def priceStock():
    stockName = textSymbol.get()
    url = "https://www.set.or.th/th/market/product/stock/quote/"+stockName+"/price"

    webopen = urlopen(url) #เปิดเว็บโดยไม่ต้องเปิด google chome
    html_page = webopen.read() #อ่านข้อมูลในเว็บ
    webopen.close() #ปิดเว็บ

    data = BeautifulSoup(html_page,"html.parser") #แปลงโค้ด 
    try:
        symbol = data.find("h1",{"class":"symbol text-white mb-0 me-2"})
        price = data.find("h1",{"class":"value text-white mb-0 me-2 lh-1"})

        symbol_stock = symbol.text.strip()
        price_stock = price.text.strip()
        print(f"ราคาหุ้น {date}")
        print(f"ชื่อ {symbol_stock}",f"ราคา {price_stock}")
        textSymbol.set("")
        messagebox.showinfo(f"ราคาหุ้น {date}",f"{symbol_stock} ราคา {price_stock} บาท ")
        E1.focus()
    except:
        print("ไม่พบข้อมูล")
        print(stockName)
        textSymbol.set("")
        E1.focus()

B1 = ttk.Button(root,text="ค้นหา",command=priceStock)
B1.pack(ipadx=20,ipady=10,pady=10)

root.mainloop()