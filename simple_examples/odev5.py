import time

class Bilgisayar():

    def __init__(self, durum = "Kapalı", donanım= [], programlar = []):
        self.durum = durum
        self.donanım = donanım
        self.programlar = programlar

    def bilgisayar_ac(self):

        if(self.durum =="Kapalı"):
            print("Bilgisayar Açılıyor...")
            time.sleep(2)
            self.durum ="Açık"
            print("HOŞGELDİNİZ")
        else:
            print("Bilgisayar zaten açık")
    def bilgisayar_kapat(self):
        if(self.durum =="Açık"):
            print("Bilgisayar kapanıyor...")
            time.sleep(2)
            self.durum ="Kapalı"
            print("BİLGİSAYAR KAPANDI")
        else:
            print("Bilgisayar zaten kapalı")
    def program_ekle(self,yeni_program):
        print("Program ekleniyor...")
        self.programlar.append(yeni_program)

    def donanım_ekle(self,donanım):
        print("Donanım ekleniyor...")
        self.donanım.append(donanım)
    def __str__(self):
        return "PC durum = {}\nDonanımlar = {}\nProgramlar = {}".format(self.durum,self.donanım,self.programlar)
    
    


print("""
1- Program Ekle

2- Bilgisayar Aç
      
3- Bilgisayar Kapat
      
4- Bilgisayar Bilgileri
      
5- Donanım Ekle
      
Çıkmak için q basın...
""")

bilgisayar1 = Bilgisayar()


while(True):

    islem = input("İşlem seçiniz: ")

    if(islem=="1"):
        program = input("Program adı giriniz: ")
        print("Program ekleniyor..")
        time.sleep(2)
        bilgisayar1.program_ekle(program)
        print("Program başarıyla eklendi.")
    elif(islem=="2"):
        bilgisayar1.bilgisayar_ac()
    elif(islem=="3"):
        bilgisayar1.bilgisayar_kapat()
    elif(islem=="4"):
        print(bilgisayar1)
    elif(islem=="5"):
        donanım = input("Eklemek istediğiniz donanınm = ")
        bilgisayar1.donanım_ekle(donanım)
    elif(islem=="q"):
        print("Çıkılıyor...")
        break
    else:
        print("Geçersiz işlem!")