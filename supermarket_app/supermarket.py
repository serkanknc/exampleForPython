import sqlite3

class Market():
    def __init__(self,urun_adi,kategori,marka,tuketici,aciklama,fiyat):
        self.urun_adi = urun_adi
        self.kategori = kategori
        self.marka = marka
        self.tuketici = tuketici
        self.aciklama = aciklama
        self.fiyat = fiyat
    
    def __str__(self):
        
        return f"Ürün adı:{self.urun_adi}\nKategori: {self.kategori}\nMarka: {self.marka}\nTuketici:{self.tuketici}\nAçıklama: {self.aciklama}\nFiyat:{self.fiyat}\n"
    

class SuperMarket():

    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):

        self.baglanti = sqlite3.connect("supermarket.db")
        self.cursor = self.baglanti.cursor()

        sorgu = "create table if not exists urunler (urunadi text, kategori text, marka text, tuketici text, aciklama text, fiyat int)"

        self.cursor.execute(sorgu)
        self.baglanti.commit()
    
    def baglanti_kes(self):
        self.baglanti.close()

    def urun_listele(self):

        sorgu = "select * from urunler"
        self.cursor.execute(sorgu)

        urunler = self.cursor.fetchall()

        if(len(urunler)==0):
            print("Herhangi bir ürün bulunamadı.")
        else:
            for i in urunler:
                urun = Market(i[0],i[1],i[2],i[3],i[4],i[5])
                print(urun)
    def urun_sorgula(self,kategori):

        sorgu = "select * from urunler where kategori = ?"
        self.cursor.execute(sorgu,(kategori,))
        urunler = self.cursor.fetchall()
        if(len(urunler)==0):
            print("Ürün bulunamadı.")
        else:
            urun = Market(urunler[0][0],urunler[0][1],urunler[0][2],urunler[0][3],urunler[0][4],urunler[0][5])
            print(urun)
    def urun_ekle(self,urun):
        sorgu = "insert into urunler values (?,?,?,?,?,?)"
        self.cursor.execute(sorgu,(urun.urun_adi,urun.kategori,urun.marka,urun.tuketici,urun.aciklama,urun.fiyat))
        self.baglanti.commit()

    def urun_sil(self,urun_adi):
        sorgu = "delete from urunler where urunadi = ?"
        self.cursor.execute(sorgu,(urun_adi,))
        self.baglanti.commit()

    def fiyat_hesapla(self):
        sorgu = "select sum(fiyat) from urunler"
        self.cursor.execute(sorgu)
        toplam_fiyat = self.cursor.fetchone()
        for i in toplam_fiyat:
            print("Ürünlerin toplam fiyatı: ",i)