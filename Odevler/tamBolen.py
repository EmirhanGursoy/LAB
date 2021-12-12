sayi = int(input("Bir sayi girin:"))
tamBolen = []
for i in range(1,sayi + 1):
    if sayi % i == 0:
        tamBolen.append(i)
        tamBolen.append(-i)
        tamBolen.sort()
        
print("Sayinin tam bolenleri:",tamBolen)