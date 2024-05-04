import random
import time
class Kumanda():

    def __init__(self,tv_durum="Kapalı", tv_ses=0,kanal_listesi=["FB TV","TRT"],kanal="FB TV"):
        self.tv_durum= tv_durum
        self.tv_ses= tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal
    
    def tv_ac(self):

        if(self.tv_durum=="Açık"):
            print("TV zaten açık.")
        else:
            print("TV açılıyor..")
            time.sleep(2)
            self.tv_durum="Açık"
            print("TV açıldı.")
    def tv_kapat(self):
        if(self.tv_durum=="Kapalı"):
            print("TV zaten kapalı.")
        else:
            print("Tv kapanıyor..")
            time.sleep(2)
            self.tv_durum="Kapalı"
            print("TV kapandı.")
    def ses_ayarlari(self):

        while(True):

            cevap = input("Sesi Azalt: '+'\nSesi Artır: '-'\nÇıkış için q basın\nSeçiniz: ")

            if(cevap=="+"):
                if(self.tv_ses !=31):
                    self.tv_ses +=1
                    print("Tv sesi : ",self.tv_ses)
            elif(cevap=="-"):
                if(self.tv_ses !=0):
                    self.tv_ses -=1
                    print("Tv sesi : ",self.tv_ses)
            elif(cevap =="q"):
                print("Menüden çıkılıyor..")
                time.sleep(2)
                break
            else:
                print("Ses güncellendi: ", self.tv_ses)
                break
    def kanal_ekle(self,kanal_ismi):
        print("Kanal ekleniyor..")
        self.kanal_listesi.append(kanal_ismi)
        print("Kanal başarıyla eklendi.")
    def kanal_sil(self,kanal_numarasi):
        print("Kanal siliniyor...")
        time.sleep(2)
        self.kanal_listesi.pop(kanal_numarasi-1)
    def rastgele_kanal(self):

        rastgele = random.randint(0,len(self.kanal_listesi)-1)

        self.kanal = self.kanal_listesi[rastgele]

        print("Şuanki kanal : ", self.kanal)
    def __len__(self):

        return len(self.kanal_listesi)
    def __str__(self):
        return "Tv durum : {}\nTv Ses: {}\nKanal Listesi {}\nŞu anki kanal {}:".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)
    

kumanda = Kumanda()

print("""
Televizyon Uygulaması

1. Tv Aç

2. Tv Kapat

3. Ses Ayarları

4. Kanal Ekle
      
5. Kanal Sil

6. Kanal Sayısını Öğrenme

7. Rastgele Kanala Geçme

8. Televizyon Bilgileri

Çıkmak için 'q' ya basın.
""")


while(True):



    islem = input("İşlem seçiniz: ")

    if(islem=="q"):
        print("Programdan çıkılıyor..")
        break
    elif(islem=="1"):
        kumanda.tv_ac()
    elif(islem=="2"):
        kumanda.tv_kapat()
    elif(islem=="3"):
        kumanda.ses_ayarlari()
    elif(islem=="4"):
        print("-----Kanal Ekleme Menüsüne Hoşgeldiniz-----")
        while(True):
            secim = input("1-Kanal Ekle\n2-Çıkış için q basın\n")
            if(secim =="q"):
                print("Kanal ekleme menüsünden çıkılıyor..")
                time.sleep(2)
                break
            else:
                kanal_adi = input("Eklenecek kanal adı : ")
                kumanda.kanal_ekle(kanal_adi)
    elif(islem=="5"):
        kanal_numarasi= int(input("Silinecek kanal numarası: "))
        kumanda.kanal_sil(kanal_numarasi)
    elif(islem=="6"):
        
        print("Kanal sayısı: ", len(kumanda))
    elif(islem=="7"):
        kumanda.rastgele_kanal()
    elif(islem=="8"):
        print(kumanda)
    else:
        print("Geçersiz işlem...")
            

        