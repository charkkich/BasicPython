from songline import Sendline
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.request import urlopen

date = datetime.now().strftime("%d-%b-%Y")

symbolStock = ["PTT","WHA","CPALL","AOT","BANPU"]
def priceStock(name):
    url = "https://www.set.or.th/th/market/product/stock/quote/"+name+"/price"

    webopen = urlopen(url) #เปิดเว็บโดยไม่ต้องเปิด google chome
    html_page = webopen.read() #อ่านข้อมูลในเว็บ
    webopen.close() #ปิดเว็บ

    data = BeautifulSoup(html_page,"html.parser") #แปลงโค้ด 
    try:
        symbol = data.find("h1",{"class":"symbol text-white mb-0 me-2"})
        price = data.find("h1",{"class":"value text-white mb-0 me-2 lh-1"})

        symbol_stock = symbol.text.strip()
        price_stock = price.text.strip()

        token = "2zfgL9qCgZxionD2LLr9w7tBH5Xdr2snnf9PqrZj7lr"
        messenger = Sendline(token)
        messenger.sendtext(f" {date} \n {symbol_stock} ราคา {price_stock} บาท") 

    except:
        print("ไม่พบข้อมูล")

for i in symbolStock:
    priceStock(i)
