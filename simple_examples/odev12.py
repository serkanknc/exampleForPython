"""
"Kareler" isminde bir tane sınıf tanımlayın ve bu sınıfı iterable bir sınıf yapmaya çalışın. 
Bu sınıfın init fonksiyonu maksimum isimli bir tane parametre alsın ve her next işleminde ekrana üzerinde bulunduğunuz sayının karesi yazdırılsın. 
StopIteration hatası ekrana maksimum sayıyı geçtiğiniz zaman fırlatılsın.
"""

class Kareler():
    def __init__(self,max= 0):
        self.max = max
        self.index = 1

    def __iter__(self):
        return self
    def __next__(self):

        
        if(self.index <=self.max):
            sonuc = self.index **2
            self.index +=1
            return sonuc
        else:
            self.index =1
            raise StopIteration

        
  

kare_al = Kareler(7)
iterator = iter(kare_al)

for i in iterator:
    print(i)

