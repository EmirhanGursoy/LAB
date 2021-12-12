
def faktoriyel(sayi):
    fakto = 1
    if sayi < 0:
        return "Negatif sayilarin faktoriyeli hesaplanamaz!!!"
    elif sayi == 0:
        return 1
    else:
        for i in range(1,sayi+1):
            fakto *= i
        return fakto
sayi = int(input("Faktoriyelini hesaplamak istediginiz sayi:"))
a = faktoriyel(sayi)
print(a)