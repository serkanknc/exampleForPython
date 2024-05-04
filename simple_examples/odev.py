#Problem 1
#Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. Ekrana yazdırma işlemini *format* metoduyla yapmaya çalışın.
"""
s1= int(input("1.sayıyı girin: "))
s2= int(input("2.sayıyı girin: "))
s3= int(input("3.sayıyı girin: "))

carpim = (s1*s2*s3)

print("3 sayının çarpımı: {}".format(carpim))
"""
#Problem 2
#Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.
#Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)

"""

boy = float(input("Boy giriniz: "))
kilo = int(input("Kilo giriniz: "))

kitleindeks = (kilo/(boy**2))

print("VÜcut kitle endeksi: {} ".format(kitleindeks))
"""

#Problem 3
#Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.

"""

gidilenmesafe = int(input("Kaç km yol yaptınız: "))
kmbasina = float(input("Km başına kaç TL yakıyor? "))

toplamodeme = (gidilenmesafe*kmbasina)

print("Toplam ödemeniz gereken tutar: {}".format(toplamodeme))
"""
#Problem 4
#Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın.


"""
ad = input("Adınız: ")
soyad = input("Soyadınız: ")
numara = input("Numaranız: ")

print("\n-----------------Bilgileriniz----------------\n")

print("Adınız: {}\nSoyadınız: {}\nNumaranız: {} ".format(ad,soyad,numara))

"""

#Problem 5
#Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.

"""

s1= int(input("1.sayıyı giriniz: "))
s2=int(input("2.sayıyı giriniz: "))

s1,s2=s2,s1

print("1.sayı {}\n2.sayı: {}".format(s1,s2))
"""

#Problem 6
#Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.
#Hipotenüs Formülü: a^2 + b^2 = c^2

a=int(input("1.dik kenar girin: "))
b= int(input("2.dik kenar girin: "))
hipotenus = (a**2+b**2)

print("Hipotenüs uzunluğu:", (hipotenus**0.5))