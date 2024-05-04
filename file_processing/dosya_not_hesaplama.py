def not_hesapla(satir):

    satir = satir[:-1]
    liste = satir.split(",")
    
    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])

    sonuc = not1* (3/10) + not2 * (3/10) + not3 * (4/10)
    
    if(sonuc>=90):
        harf = "AA"
    elif(sonuc>=85):
        harf ="BA"
    elif(sonuc>=80):
        harf ="BB"
    elif(sonuc>=75):
        harf ="CB"
    elif(sonuc>=70):
        harf ="CC"
    elif(sonuc>=65):
        harf ="DC"
    elif(sonuc>=60):
        harf ="DD"
    elif(sonuc>=55):
        harf ="FD"
    else:
        harf = "FF"

    return isim + " => " + harf + "\n"

with open("C:/Users/serkan/Desktop/dosya.txt","r",encoding="utf-8") as file:

    eklenecekler = []

    for i in file:
        eklenecekler.append(not_hesapla(i))

    with open("C:/Users/serkan/Desktop/tum_notlar.txt","w",encoding="utf-8") as file2:

        for i in eklenecekler:
            file2.write(i)
            
    with open("C:/Users/serkan/Desktop/tum_notlar.txt","r",encoding="utf-8") as file3:
        kalanlar =[]
        gecenler = []

        for i in file3:
            i = i[:-1]
            satir_eleman = i.split(" => ")

            if(satir_eleman[1]=="FF"):
                kalanlar.append(i+"\n")
            else:
                gecenler.append(i+"\n")

    with open("C:/Users/serkan/Desktop/kalanlar.txt","w",encoding="utf-8") as file4:
        for i in kalanlar:
            file4.write(i)
    with open("C:/Users/serkan/Desktop/gecenler.txt","w",encoding="utf-8") as file4:
        for i in gecenler:
            file4.write(i)