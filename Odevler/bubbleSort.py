def bubbleSort(Liste):
    n = len(Liste)

    for i in range(n-1):
        for j in range(0, n-i-1):
            if Liste[j] > Liste[j + 1] :
                Liste[j], Liste[j + 1] = Liste[j + 1], Liste[j]
Liste = [64, 34, 25, 12, 22, 11, 90]
 
bubbleSort(Liste)
 
print (Liste)
