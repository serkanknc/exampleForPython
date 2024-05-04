import math


print("""
Üs almak için = 1
Sayının karekökünü almak için = 2
Sayının logaritması için = 3
dereceyi radyana çevirmek için = 4
radyanı dereceye çevirmek için = 5
sinüs ü bulmak için = 6
cos u bulmak için = 7
tanjantı bulmak için = 8
cotanjantı bulmak için = 9
Çıkmak için q ya basın...
""")


while True:
    islem = input("Seçim yapınız: ")

    if(islem =="q"):
        print("Programdan çıkılıyor")
        break
    elif(islem=="1"):
        sayi1=int(input("Sayıyı giriniz: "))
        sayi2= int(input("Üssü giriniz: "))
        x = math.pow(sayi1,sayi2)
        print("{} üssü {}  = {} dır".format(sayi1,sayi2,x))
    elif(islem=="2"):
        sayi1=int(input("Sayıyı giriniz: "))
        x=math.sqrt(sayi1)
        print("{} sayısının karekökü {} dır".format(sayi1,x))
    elif(islem=="3"):
        sayi1= int(input("Sayıyı giriniz: "))
        sayi2=int(input("Logaritma tabanını giriniz: "))
        x= math.log(sayi1,sayi2)
        print("{} sayısının logaritması {} dır".format(sayi1,x))
    elif(islem=="4"):
        sayi1=int(input("Sayıyı giriniz: "))
        x= math.radians(sayi1)
        print("{} derece {} radyanttır".format(sayi1,x))
    elif(islem=="5"):
        sayi1=int(input("Sayıyı giriniz: "))
        x= math.degrees(sayi1)
        print("{} radyant {} derecedir".format(sayi1,x))
    elif(islem=="6"):
       
       a= input("Radyan için = R, Derece için = D ")

       if(a=="r" or a=="R"):
            sayi1=int(input("Radyan giriniz: "))
            x=math.sin(sayi1)
            print("{} radyan = sin {}".format(sayi1,x))
       elif(a=="d" or a=="D"):
            sayi1=int(input("Derece giriniz: "))
            x= math.radians(sayi1)
            y= math.sin(x)
            print("{} derece = sin {}".format(sayi1,y))
    elif(islem=="7"):
        a= input("Radyan için = R, Derece için = D ")

        if(a=="r" or a=="R"):
           sayi1=int(input("Radyan giriniz: "))
           x=math.cos(sayi1)
           print("{} radyan = cos {}".format(sayi1,x))
        
        elif(a=="d" or a=="D"):
           sayi1=int(input("Derece giriniz: "))
           x= math.radians(sayi1)
           y= math.cos(x)
           print("{} derece = cos {}".format(sayi1,y))
    elif(islem=="8"):

        a= input("Radyan için = R, Derece için = D ")

        if(a=="r" or a=="R"):
           sayi1=int(input("Radyan giriniz: "))
           x=math.tan(sayi1)
           print("{} radyan = tan {}".format(sayi1,x))
        
        elif(a=="d" or a=="D"):
           sayi1=int(input("Derece giriniz: "))
           x= math.radians(sayi1)
           y= math.tan(x)
           print("{} derece = tan {}".format(sayi1,y))
    elif(islem=="9"):

        a= input("Radyan için = R, Derece için = D ")

        if(a=="r" or a=="R"):
           sayi1=int(input("Radyan giriniz: "))
           x=math.cos(sayi1)/math.sin(sayi1)
           print("{} radyan = cot {}".format(sayi1,x))
        
        elif(a=="d" or a=="D"):
           sayi1=int(input("Derece giriniz: "))
           x= math.radians(sayi1)
           y= math.cos(x)/math.sin(x)
           print("{} derece = cot {}".format(sayi1,y))


        