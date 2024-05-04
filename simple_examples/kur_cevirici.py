import requests 
from bs4 import BeautifulSoup
import sys

url = "https://www.doviz.com"
response = requests.get(url)
html_ierik = response.text

soup = BeautifulSoup(html_ierik, "html.parser")

dolar_kuru = soup.find("span", {"data-socket-key": "USD"})
euro_kuru = soup.find("span", {"data-socket-key": "EUR"})
sterlin_kuru = soup.find("span", {"data-socket-key": "GBP"})
gram_altin = soup.find("span", {"data-socket-key": "gram-altin"})
bist = soup.find("span", {"data-socket-key": "XU100"})


print("DÖVİZ PROGRAMINA HOŞGELDİNİZ")
while True:

    print(   """
1. DOLAR-TL HESAPLA
2. EURO-TL HESAPLA
3. STERLİN-TL HESAPLA
4. GRAM ALTIN BİLGİSİ AL
5. BIST BİLGİSİ AL

Çıkmak için 'q' basın...
************************************
""")
    
    secim = input("İşlem seçiniz: ")

    if(secim=="q"):
        sys.exit()
    elif(secim=="1"):
        sayi_dolar = float(dolar_kuru.text.replace(",","."))
        print("Güncel dolar kuru: ", sayi_dolar)
        dolar= int(input("Kaç dolar'ı TL'ye çevirmek istiyorsunuz? "))
        sonuc = dolar*sayi_dolar
        print(f"{dolar} dolar {sonuc} TL")
    elif(secim=="2"):
        sayi_euro = float(euro_kuru.text.replace(",","."))
        print("Güncel euro kur: ",sayi_euro)
        euro = int(input("Kaç euro'u TL'ye çevirmek istiyorsunuz? "))
        sonuc = euro*sayi_euro
        print(f"{euro} dolar {sonuc} TL")
    elif(secim=="3"):
        sayi_sterlin = float(sterlin_kuru.text.replace(",","."))
        print("Güncel euro kur: ",sayi_sterlin)
        sterlin = int(input("Kaç sterlin'i TL'ye çevirmek istiyorsunuz? "))
        sonuc = sterlin*sayi_sterlin
        print(f"{sterlin} dolar {sonuc} TL")
    elif(secim=="4"):
        print("Güncel gram altın: ",gram_altin.text)
    elif(secim=="5"):
        print("Güncel BIST değeri: ",bist.text)
    else:
        print("Hatalı seçim...")


