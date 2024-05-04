print("**********\nATM Uygulaması\n**********\n")

print(""" 
İşlemler

1- Bakiye Sorgulama
2. Para Yatırma
3- Para Çekme          

Programdan 'q' tuşu ile çıkabilirsiniz.

""")

bakiye= 1000

while(True):
    islem = input("İşlem seçiniz: ")

    if(islem=="q"):
        print("Programdan çıkılıyor..")
        break
    elif(islem=="1"):
        print("Bakiyeniz {} TL'dir".format(bakiye))
    elif(islem=="2"):
        para_yatir= int(input("Yatırmak istediğiniz tutar: "))
        bakiye+=para_yatir
        
    elif(islem=="3"):
        para_cek = int(input("Çekmek istediğiniz tutarı giriniz:"))

        if(bakiye-para_cek < 0):
            print("Bakiyeniz yetersiz.")
            print("Bakiyeniz {} TL' dir".format(bakiye))
            continue
        else:
            bakiye -=para_cek
        
    else:
        print("Geçerli bir işlem seçiniz.")
        