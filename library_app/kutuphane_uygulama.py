from kutuphane import *

print("""***********************************

Kütüphane Programına Hoşgeldiniz.

İşlemler;

1. Kitapları Göster

2. Kitap Sorgulama

3. Kitap Ekle

4. Kitap Sil 

5. Baskı Yükselt

Çıkmak için 'q' ya basın.
***********************************""")


kutuphane = Kutuphane()

while True:
    islem = input("İslem seçiniz: ")

    if(islem =="q"):
        print("Programdan çıkılıyor...")
        time.sleep(1)
        break
    elif(islem=="1"):
        kutuphane.kitap_goster()
        
    elif(islem=="2"):
        kitap_isim = input("Hangi kitabı listelemek istiyorsunuz? ")
        print("Kitap listeleniyor...")
        time.sleep(1)
        kutuphane.kitap_sorgula(kitap_isim)
        
    elif(islem=="3"):
        isim = input("Kitap adı: ")
        yazar = input("Yazar adı: ")
        yayinevi = input("Yayınevi: ")
        tur = input("Kitap türü: ")
        baski = int(input("Baskı no: "))

        yeni_kitap = Kitap(isim,yazar,yayinevi,tur,baski)

        print("Kitap ekleniyor...")
        time.sleep(1)
        kutuphane.kitap_ekle(yeni_kitap)
        print("Kitap eklendi.")
        
    elif(islem=="4"):
        kitap_isim = input("Hangi kitabı silmek istiyorsunuz? ")
        kutuphane.kitap_sil(kitap_isim)
        
    elif(islem=="5"):
        isim = input("Hangi kitabın baskısını yükseltmek istiyorsunuz? ")
        print("Baskı yükseltiliyor...")
        time.sleep(1)
        kutuphane.baski_yukselt(isim)
        print("Baskı yükseltildi.")
        