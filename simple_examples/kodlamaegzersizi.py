
"""2. dereceden bir bilinmeyenli denklemin köklerini bulma

Denklem : ax^2 + bx + c

Deltayı Hesaplama:  b ** 2 -  4 * a * c

Birinci Kök : (-b - delta ** 0.5) / (2*a)
İkinci Kök : (-b + delta ** 0.5) / (2*a)
"""

a= int(input("a: "))
b= int(input("b: "))
c = int(input("c: "))

delta= b**2-4*a*c

x1= (-b-delta**0.5)/(2*a)
x2= (-b+delta**0.5)/(2*a)

print("Birinci kök {}\nİkinci kök {}\n".format(x1,x2))


"-------------------------------------------------------------------------------"

print("Oyuncu Kaydetme Programı")

oyuncuadi= input("Oyuncu Adı: ")
oyuncusoyadi = input("Oyuncu Soyadı: ")
oyunutakimi = input("Oyuncu Takımı: ")

bilgiler = [oyuncuadi,oyuncusoyadi,oyunutakimi]

print("Bilgiler kaydediliyor...")

print("Oyuncu Adı {}'dır\nOyuncu Soyadı {}'dır\nOyuncu Takımı {}'dır".format(bilgiler[0],bilgiler[1],bilgiler[2]))

print("Bilgiler kaydedildi.")