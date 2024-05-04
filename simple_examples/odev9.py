from functools import reduce

#problem1

def alan_hesapla(kenarlar):

    uzunluk,genislik = kenarlar
    return uzunluk * genislik

kenarlar = [(3,4),(10,3),(5,6),(1,9)]

print("alanlar= ", list(map(alan_hesapla,kenarlar)))


#problem2

liste= [(3,4,5),(6,8,10),(3,10,7),(9,12,15)]

def ucgen_mi(demet):
    if(abs(demet[0]+ demet[1]> demet[2]) and abs(demet[0]+demet[2]> demet[1]) and abs(demet[1]+demet[2]> demet[0])):
        return True
    else:
        return False
    
print(list(filter(ucgen_mi,liste)))


#problem3

liste =  [1,2,3,4,5,6,7,8,9,10]

cift_filtre = list(filter(lambda x : x % 2==0,liste))
print(reduce(lambda x,y: x+y,cift_filtre))


#problem4

isimler = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
soyisimler = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

for i,j in zip(isimler,soyisimler):
    print(i,j)