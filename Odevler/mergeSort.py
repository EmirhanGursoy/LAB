def merge(Liste, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = Liste[l + i]
 
    for j in range(0, n2):
        R[j] = Liste[m + 1 + j]
 
    i = 0     
    j = 0     
    k = l     
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            Liste[k] = L[i]
            i += 1
        else:
            Liste[k] = R[j]
            j += 1
        k += 1
     
    while i < n1:
        Liste[k] = L[i]
        i += 1
        k += 1
  
    while j < n2:
        Liste[k] = R[j]
        j += 1
        k += 1
 
def mergeSort(Liste, l, r):
    if l < r:        
        m = l+(r-l)//2       
        mergeSort(Liste, l, m)
        mergeSort(Liste, m+1, r)
        merge(Liste, l, m, r)
 
Liste = [12, 11, 13, 5, 6, 7]
n = len(Liste)
mergeSort(Liste, 0, n-1)
print(Liste)
