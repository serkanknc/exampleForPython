"""
Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

 BKİ 18.5'un altındaysa -------> Zayıf

 BKİ 18.5 ile 25 arasındaysa ------> Normal

 BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

 BKİ 30'un üstündeyse -------------> Obez


"""


kilo = int(input("Kilonuzu giriniz: "))
boy = float(input("Boyunuzu m cinsinden giriniz: "))

bki = (kilo/(boy**2))

if(bki<18.5):
    print("Zayıfsınız.",bki)
elif(bki>=18 and bki<25):
    print("Normalsiniz.",bki)
elif(bki>=25 and bki<30):
    print("Fala kilolu",bki)
elif(bki>=30):
    print("Obez",bki)


#Problem 2
#Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.


sayi1=int(input("Birinci sayı giriniz: "))
sayi2=int(input("İkinci sayı giriniz: "))
sayi3=int(input("Üçüncü sayı giriniz: "))

if(sayi1>sayi2 and sayi1>sayi3):
    print("En büyük sayı birinci sayı", sayi1)
elif(sayi2>sayi1 and sayi2>sayi3):
    print("En büyük sayı ikinci sayı", sayi2)
elif(sayi3>sayi1 and sayi3>sayi2):
    print("En büyük sayı üçüncü sayı", sayi3)

"""
Problem 3
Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.

    Vize1 toplam notun %30'una etki edecek.

    Vize2 toplam notun %30'una etki edecek.

    Final toplam notun %40'ına etki edecek.


    Toplam Not >=  90 -----> AA

    Toplam Not >=  85 -----> BA

    Toplam Not >=  80 -----> BB

    Toplam Not >=  75 -----> CB

    Toplam Not >=  70 -----> CC

    Toplam Not >=  65 -----> DC

    Toplam Not >=  60 -----> DD

    Toplam Not >=  55 -----> FD

    Toplam Not <  55 -----> FF

"""

vize1 = int(input("1.vizeyi giriniz: "))
vize2 = int(input("2.vizeyi giriniz: "))
final = int(input("Finali giriniz: "))

toplamnot= (vize1*3/10+vize2*3/10+final*4/10)

if(toplamnot>=90):
    print("AA")
elif(toplamnot>=85):
    print("BA")
elif(toplamnot>=80):
    print("BB")
elif(toplamnot>=75):
    print("CB")
elif(toplamnot>=70):
    print("CC")
elif(toplamnot>=65):
    print("DC")
elif(toplamnot>=60):
    print("DD")
elif(toplamnot>=55):
    print("FD")
elif(toplamnot>=50):
    print("FF")


"""
Problem 4
Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.

Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.

Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın. 
Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o

Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.

Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak. Bunun için, Pythonda hazır bir fonksiyon olan abs() fonksiyonunu kullanabilirsiniz. Kullanımı şu şekildedir ;
"""
print("-------------------------------------------\nGeometrik Şekil Hesaplamaya Hoşgeldiniz\n-------------------------------------------\n")

print("Geometrik Şekiller\n1-Dörtgen\n2-Üçgen")

geometriksekil= input("Hangi geometrik şekilin tipini öğrenmek istiyorsunuz: ")

if(geometriksekil=="Dörtgen"):
    print("Lütfen kenarları giriniz:")
    a=int(input("Birinci kenar: "))
    b=int(input("İkinci kenar: "))
    c=int(input("Üçüncükenar: "))
    d=int(input("Dördüncü kenar: "))

    if(a==b and a==c and a==d):
        print("Kare")
    elif(a==c and b==d):
        print("Dikdörtgen")
    else:
        print("Sıradan dörtgen")
elif(geometriksekil=="Üçgen"):
    print("Lütfen kenarları giriniz..")
    a=int(input("Birinci kenar: "))
    b=int(input("İkinci kenar: "))
    c=int(input("Üçüncükenar: "))

    if( abs(a+b) > c and abs(a+c) > b and abs(b+c) > a):
        if(a==b and a==c):
            print("Eşkenar Üçgen")
        elif((a==b and a!=c) or (a==c and a!=b) or (b==c and b!=a)):
            print("İkizkenar üçgen")
        else:
            print("Çeşitkenar üçgen")
    else:
        print("Üçgen belirtmiyor")    
else:
    print("Geçersiz şekil")