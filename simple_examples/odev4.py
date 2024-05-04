"""
Problem 1
1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın. Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.

Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır. Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).


"""

def mukemmel_sayi (sayi):

    toplam = 0

    for i in range(1,sayi):
        if(sayi% i ==0):
            toplam+=i

    return toplam==sayi

for i in range(1,1001):
    if(mukemmel_sayi(i)):
        print("Mükemmel sayi", i)

"""
Problem 2
Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.

"""


def ebob_bulma (sayi1,sayi2):
    ebob = 1
    for i in range (1,sayi1):
        if(sayi1 % i ==0 and sayi2 % i == 0):
            ebob = i
    return ebob

sayi1= int(input("1.sayıyı giriniz: "))
sayi2= int(input("2.sayıyı giriniz: "))

print("{} ve {} sayısının EBOB'u {}' dır.". format(sayi1,sayi2, ebob_bulma(sayi1,sayi2)))





"""
Problem 3
Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK) dönen bir tane fonksiyon yazın.

"""

def ekok_bul (sayi1,sayi2):
    i=2
    ekok = 1

    while True:

        if (sayi1 % i == 0 and sayi2 % i == 0):
            ekok *= i

            sayi1 //= i
            sayi2 //= i


        elif (sayi1 % i ==  0 and sayi2 % i != 0):
            ekok *= i

            sayi1 //= i


        elif (sayi1 % i != 0 and sayi2 % i == 0):
            ekok *= i

            sayi2 //= i
        else:
            i += 1
        if (sayi1 == 1 and sayi2 == 1):
            break
    return ekok

sayi1= int(input("1.sayıyı giriniz: "))
sayi2= int(input("2.sayıyı giriniz: "))
        
print("{} ve {} sayısının ekoku {}' dır".format(sayi1,sayi2,ekok_bul(sayi1,sayi2)))


"""
Problem 4
Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.

Örnek: 97 ---------> Doksan Yedi
"""

birler =  ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]

def sayi_okunus (sayi):
    birinci = sayi % 10
    ikinci = sayi // 10
    
    return onlar[ikinci] + " " + birler[birinci]

sayi = int(input("Sayı : "))

print(sayi_okunus(sayi))