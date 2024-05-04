"""
def karakter_frekansi():
    stringimiz = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"

    karakterler = list()

    for i in stringimiz:
        karakterler.append(i)

    karakter_sozluk = dict()

    for i in karakterler:
        
        if(i in karakter_sozluk):
            karakter_sozluk[i] +=1
        else:
            karakter_sozluk[i] = 1
        
    for kelime,sayi in karakter_sozluk.items():
        print(f"{kelime} harfi {sayi} defa geçiyor")

karakter_frekansi()

"""
"""
def kelime_birlestirme():
    
    with open("şiir.txt","r",encoding="utf-8") as file:
        ilk_karakterler = list()
        for i in file:
            ilk_karakterler.append(i[0])
        
        birlestirme_string = "".join(ilk_karakterler)
        print(birlestirme_string)

kelime_birlestirme()

"""
"""
def mail_format_uygunmu():

    with open("mailler.txt","r",encoding="utf-8") as file:
        
        for i in file:
            i = i.strip("\n")
            if(i.endswith(".com") and i.find("@")!=-1):
                print(i)
        
mail_format_uygunmu()  
"""

isim = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

soyisim = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
  
liste= list(zip(isim,soyisim))
liste.sort()

for i,j in liste:
    print(i,j)


