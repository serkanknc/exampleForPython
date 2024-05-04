def ekstra(fonksiyon):

    def wrapper(sayilar):

        cift_sayilar= 0 
        ciftler_toplami = 0
        tek_sayilar = 0
        tekler_toplami = 0

        for i in sayilar:
            if (i % 2 ==0):
                ciftler_toplami += i
                cift_sayilar += 1
            else:
                tekler_toplami += i
                tek_sayilar +=1
        print("Çiftlerin ortalaması: ",ciftler_toplami/cift_sayilar)
        print("Teklerin ortalaması: ",tekler_toplami/tek_sayilar)

        fonksiyon(sayilar)
    return wrapper

@ekstra
def ortalama_bul(sayilar):

    toplam = 0 

    for sayi in sayilar:
        toplam += sayi
    print("Ortalama: ",toplam/len(sayilar))

ortalama_bul([1,2,4,5,88,10,100,200,150,64,31,41,55,73,180,19])