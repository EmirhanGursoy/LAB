def insertionSort(Liste):
 
    for i in range(1, len(Liste)):
  
        key = Liste[i]
  
        j = i-1
        while j >=0 and key < Liste[j] :
                Liste[j+1] = Liste[j]
                j -= 1
        Liste[j+1] = key
  
Liste = [12, 11, 13, 5, 6]
insertionSort(Liste)
print(Liste)