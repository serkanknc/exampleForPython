print("**********\nKullanıcı Girişi\n**********\n")

sys_kullaniciadi = "serkan"
sys_sifre = "1234"


giris_hakki=3

while(True):
    kullaniciadi = input("Kullanıcı adınızı girinz: ")
    sifre = input("Şifre giriniz: ")

    if(sys_kullaniciadi!=kullaniciadi and sys_sifre==sifre):
        print("Kullanıcı adı hatalı..")
        giris_hakki-=1
        print("Kalan giriş hakkı: ",giris_hakki)
    elif(sys_kullaniciadi==kullaniciadi and sys_sifre!=sifre):
        print("Şifre hatalı..")
        giris_hakki-=1
        print("Kalan giriş hakkı: ",giris_hakki)
    elif(sys_kullaniciadi!= kullaniciadi and sys_sifre!=sifre):
        print("Kullanıcı adı ve şifre hatalı..")
        giris_hakki-=1
        print("Kalan giriş hakkı: ",giris_hakki)
    else:
        print("Başarıyla giriş yaptınız.")
    if(giris_hakki==0):
        print("Giriş hakkınız bitti.")
        break
    
