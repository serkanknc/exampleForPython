liste = ["345","sadas","324a","14","kemal"]

for eleman in liste:

    try:
        eleman = int(eleman)
        print(eleman)
    
    except:
        pass


def cift_mi(sayi):

    if(sayi % 2==0):
        return sayi
    else:
        raise ValueError
    
liste = [57,2,1,3,88,102,61,2000]


for eleman in liste:

    try:
        print(cift_mi(eleman))
    except ValueError:
        pass