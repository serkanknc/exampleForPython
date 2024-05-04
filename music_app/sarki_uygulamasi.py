from sarki import *



sarkikitaplik = SarkiKitaplik()

while(True):

    print("""***********************************

Şarkı Programına Hoşgeldiniz.

İşlemler;

1. Şarkıları Göster

2. Şarkı Ekle

3. Şarkı Sil 
      
4. Tüm şarkıların toplam süresini hesapla

Çıkmak için 'q' ya basın.
***********************************""")

    islem =input("Bir işlem seçiniz: ")

    if(islem=="q"):
        print("Programdan çıkılıyor...")
        time.sleep(1)
        break
    elif(islem=="1"):
        print("Şarkılar listeleniyor...")
        time.sleep(1)

        sarkikitaplik.sarki_listele()
    
    elif(islem=="2"):

        sarki_adi= input("Şarkı adı: ")
        sanatci= input("Sanatçı adı: ")
        album= int(input("Albüm Yıl: "))
        produksiyon= input("Prodüksyion: ")
        sarki_suresi= int(input("Şarkı süresi(dk) : "))

        yeni_sarki = Sarki(sarki_adi,sanatci,album,produksiyon,sarki_suresi)
        
        print("Şarkı ekleniyor...")
        time.sleep(1)
        sarkikitaplik.sarki_ekle(yeni_sarki)
        print("Şarkı eklendi.")

    elif(islem=="3"):
        isim= input("Silmek istediğiniz şarkı adı: ")

        print("Şarkı siliniyor...")
        time.sleep(1)
        sarkikitaplik.sarki_sil(isim)
        print("Şarkı silindi.")
    
    elif(islem=="4"):
        print("Toplam şarkı süreleri hesaplanıyor...")
        time.sleep(1)

        sarkikitaplik.toplam_sarki_suresi()
