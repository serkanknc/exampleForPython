"""
Fibonacci Serisi yeni bir sayıyı önceki iki sayının toplamı şeklinde oluşturur.

1,1,2,3,5,8,13,21,34...............
"""
ilk_sayi= 1
ikinci_sayi=1

fobonacii= [ilk_sayi,ikinci_sayi]

for i in range(10):
    ilk_sayi,ikinci_sayi = ikinci_sayi,ilk_sayi+ikinci_sayi
    fobonacii.append(ikinci_sayi)
print(fobonacii)