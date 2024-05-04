import random
import time

rastgele_sayi = random.randint(1,1001)
tahmin_hakki = 10

while True:
    tahmin= int(input("Tahmininiz: "))

    if(tahmin< rastgele_sayi):
        print("Kontrol ediliyor...")
        time.sleep(1)
        print("Daha yüksek bir sayı söyleyin.")

        tahmin_hakki-=1

    elif (tahmin>rastgele_sayi):

        print("Kontrol ediliyor...")
        time.sleep(1)
        print("Daha düşük bir sayı söyleyin.")

        tahmin_hakki-=1
    else:
        print("Konrol ediliyor..")
        time.sleep(1)
        print("Tebrikler doğru tahmin. ",rastgele_sayi)
        break
    if(tahmin_hakki==0):
        print("Tahmin hakkınız bitti")
        print("Sayımız: ",rastgele_sayi)
        break