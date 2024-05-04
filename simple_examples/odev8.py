

with open("C:/Users/serkan/Desktop/futbolcular.txt","r",encoding="utf-8") as file:

    fb= list()
    bjk = list()
    hty= list()

    for i in file:
        i = i[:-1]
        satir_eleman = i.split(",")

        if(satir_eleman[1]=="Fenerbahçe"):
            fb.append(i+"\n")
        elif(satir_eleman[1]=="Beşiktaş"):
            bjk.append(i+"\n")
        else:
            hty.append(i+"\n")
    
    with open("C:/Users/serkan/Desktop/fb.txt","w",encoding="utf-8") as file2:
        for i in fb:
            file2.write(i)

    with open("C:/Users/serkan/Desktop/bjk.txt","w",encoding="utf-8") as file3:
        for i in bjk:
            file3.write(i)
    with open("C:/Users/serkan/Desktop/hty.txt","w",encoding="utf-8") as file4:
        for i in hty:
            file4.write(i)


