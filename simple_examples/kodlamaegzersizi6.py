
#?Asal Sayılar : 1'e ve kendisinden başka sayıya bölünmeyen sayılardır.


def asal (sayi):
    if(sayi==1):
        return False
    elif (sayi==2):
        print("NOT: 2 sayısı çift olan tek asal sayıdır.")
        return True
    else:
        for i in range(2,sayi):
            if(sayi%i==0):
                return False
            else:
                return True


while True:
    sayi = input("Sayı: ")

    if(sayi=="q"):
        print("Programdan çıkıldı..")
        break
    else:
        sayi= int(sayi)

        if(asal(sayi)):
            print("Girilen {} sayısı asal.".format(sayi))
        else:
            print("{} sayısı asal değildir.".format(sayi))


