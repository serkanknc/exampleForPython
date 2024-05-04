
#todo Tam bölenleri Bulma 


def tamBolenler(sayi):
    tam_bolenler= []

    for i in range(1,sayi+1):

        if(sayi % i == 0):
            tam_bolenler.append(i)
    return tam_bolenler


while True:

    sayi = input("Sayı giriniz: ")

    if(sayi == "q"):
        print("Programdan çıkıldı..")
        break
    else:
        sayi = int(sayi)

        print("Tam bölenler: ", tamBolenler(sayi))