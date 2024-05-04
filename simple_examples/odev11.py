def decaro(fonksiyon):

    def wrapper():
        print("------MÜKEMMEL SAYILAR------")
        
        for sayi in range(1,1001):
            toplam= 0
            for i in range(1,sayi):
                if(sayi % i) ==0:
                    toplam +=i
            if(toplam==sayi):
                print(sayi)
        print("--------------")
        fonksiyon()
    return wrapper
 
@decaro
def asal_bul():
    for sayi in range(1,1001):
        if(sayi>1):
            for i in range(2,sayi):
                if(sayi % i== 0) :
                    break
            else:
                print(sayi)

asal_bul()
