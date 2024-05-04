from supermarket import*


print("""***********************************

Supermarket Programına Hoşgeldiniz.

İşlemler;

1. Ürün Listele

2. Ürün kategori sorgula

3. Ürün Ekle
      
4. Ürün sil
      
5. Ürünlerin toplam fiyatını hesapla

Çıkmak için 'q' ya basın.
***********************************""")


market = SuperMarket()

while(True):

    secim = input("İşlem seçiniz: ")
    print("******************------------******************")

    if(secim=="q"):
        print("Programdan çıkılıyor...")
        break

    elif(secim=="1"):
        market.urun_listele()

    elif(secim=="2"):
        kategori = input("Kategori adı giriniz: ")
        market.urun_sorgula(kategori)
    
    elif(secim=="3"):
        urun_adi = input("Ürün adı: ")
        kategori = input("Kategori: ")
        marka = input("Marka: ")
        tuketici = input("Tuketici tipi(E/K): ")
        aciklama = input("Ürün açıklaması: ")
        fiyat = int(input("Fiyat(TL): "))

        urun = Market(urun_adi,kategori,marka,tuketici,aciklama,fiyat)
        market.urun_ekle(urun)

    elif(secim=="4"):
        urun_adi= input("Silmek istediğiniz ürün adı: ")
        market.urun_sil(urun_adi)
    elif(secim=="5"):
        market.fiyat_hesapla()


