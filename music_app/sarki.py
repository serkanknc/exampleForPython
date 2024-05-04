import sqlite3
import time

class Sarki():
    def __init__(self,sarki_isim,sanatci,album,produksiyon,sarki_suresi):
        self.sarki_isim = sarki_isim
        self.sanatci = sanatci
        self.album = album
        self.produksiyon = produksiyon
        self.sarki_suresi = sarki_suresi
    
    def __str__(self):

        return f"Şarkı adı: {self.sarki_isim}\nSanatçı: {self.sanatci}\nAlbüm: {self.album}\nProdüksyion: {self.produksiyon}\nŞarkı süresi: {self.sarki_suresi}\n"
    
class SarkiKitaplik():

    def __init__(self):

        self.baglanti_olustur()
    
    def baglanti_olustur(self):

        self.baglanti = sqlite3.connect("sarki_kitapligi.db")
        self.cursor = self.baglanti.cursor()

        sorgu = "create table if not exists sarkilar (sarki_isim text, sanatci text, album int, produksiyon text, sarki_suresi int)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()
    
    def baglanti_kes(self):
        self.baglanti.close()

    def sarki_ekle(self,sarki):
        sorgu = "insert into sarkilar values (?,?,?,?,?)"

        self.cursor.execute(sorgu,(sarki.sarki_isim,sarki.sanatci,sarki.album,sarki.produksiyon,sarki.sarki_suresi))
        self.baglanti.commit()
    
    def sarki_sil(self,sarki_isim):
        sorgu = "delete from sarkilar where sarki_isim = ?"

        self.cursor.execute(sorgu,(sarki_isim,))
        self.baglanti.commit()
    
    def sarki_listele(self):
        sorgu = "select * from sarkilar"

        self.cursor.execute(sorgu)
        sarkilar = self.cursor.fetchall()

        if(len(sarkilar)==0):
            print("Kitaplıkta şarkı bulunamadı.")
        else:
            for i in sarkilar:
                sarki = Sarki(i[0],i[1],i[2],i[3],i[4])
                print(sarki)

    def toplam_sarki_suresi(self):
        
        sorgu="select sum(sarki_suresi) from sarkilar"
        self.cursor.execute(sorgu)

        toplam_dakika = self.cursor.fetchone()
        for i in toplam_dakika:
            print("Toplam şarkı dakikası:", i)

        



        
        

        