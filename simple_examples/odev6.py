
class Hayvan():
    
    def __init__(self,cins,isim,ses,renk): 
        self.cins = cins
        self.isim = isim
        self.ses = ses
        self.renk = renk
class Kopek(Hayvan):

    def __init__(self, cins, isim, ses, renk, koku_alma_orani):
        super().__init__(cins, isim, ses, renk)

        self.kokualma = koku_alma_orani

    def kopek_otme(self):

        print("Köpek havladı.")

class Kus(Hayvan):

    def __init__(self, cins, isim, ses, renk, gaga_tipi):
        super().__init__(cins, isim, ses, renk)
        self.gaga = gaga_tipi

    def kus_otme(self):

        print("Kuş öttü.")

class At(Hayvan):

    def __init__(self, cins, isim, ses, renk, nal_tipi):
        super().__init__(cins, isim, ses, renk)
        self.nal = nal_tipi

    def at_kisneme(self):
        print("At kişnedi.")