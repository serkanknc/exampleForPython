print("""-------------------------------------------------
Hesap Makinesi Programına Hoşgeldiniz 
İşlemler;

1. Toplama İşlemi

2. Çıkarma İşlemi

3. Çarpma İşlemi

4. Bölme İşlemi
-----------------------------------------------------------
""") 



"""

sayi1= int(input("Birinci sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))

islem= int(input("İşlem numarası giriniz: "))

sonuc= 0

if(islem==1):
    sonuc=sayi1+sayi2
    print("İşlemin sonucu: {}".format(sonuc))
elif(islem==2):
    sonuc= sayi1-sayi2
    print("İşlemin sonucu: {}".format(sonuc))
elif(islem==3):
    sonuc=sayi1*sayi2
    print("İşlemin sonucu: {}".format(sonuc))
elif(islem==4):
    sonuc=sayi1/sayi2
    print("İşlemin sonucu: {}".format(sonuc))
else:
    print("Geçersiz işlem seçtiniz.")
"""
"""
sys_kullaniciadi="serkan"
sys_sifre ="1234"

kullaniciadi=input("Kullanıcı adı giriniz: ")
sifre= input("Sifre giriniz: ")

if(sys_kullaniciadi!= kullaniciadi and sys_sifre==sifre):
    print("Kullanıcı adı hatalı.")
elif(sys_sifre!=sifre and sys_kullaniciadi==kullaniciadi):
    print("Sifre hatalı.")
elif(sys_kullaniciadi!=kullaniciadi and sys_sifre!=sifre):
    print("Kullanıcı adı ve şifre hatalı.")
else:
    print("Başarıyla giriş yaptınız.")

"""

