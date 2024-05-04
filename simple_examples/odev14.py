import os
"""
Bilgisayarınızdaki tüm mp4,txt ve pdf dosyalarını os modülüyle arayın ve bunların nerede bulunduklarını ve isimlerini ayrı ayrı 
"pdf_dosyalari.txt","mp4_dosyaları.txt","txt_dosyaları.txt" adlı dosyalara kaydedin.
"""
txtdosyalari=[]
txtdosyayolu = []
with open("C:/Users/monster/Desktop/txtdosyalari.txt","w",encoding="utf-8") as file:

    for klasör_yolu,klasör_isimleri,dosya_isimleri in os.walk("C:"):

        for d_isim in dosya_isimleri:
            if(d_isim.endswith(".txt")):
                txtdosyalari.append(d_isim)
    for j in txtdosyalari:
        file.write("Dosya adı: "+ j +"\n")
 


