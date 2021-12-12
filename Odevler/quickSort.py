def partition(liste, low, high):
    i = (low-1)         
    pivot = liste[high]     
 
    for j in range(low, high):
 
        if liste[j] <= pivot:

            i = i+1
            liste[i], liste[j] = liste[j], liste[i]
 
    liste[i+1], liste[high] = liste[high], liste[i+1]
    return (i+1)

 
def quickSort(liste, low, high):
    if len(liste) == 1:
        return liste
    if low < high:

        pi = partition(liste, low, high)
 
        quickSort(liste, low, pi-1)
        quickSort(liste, pi+1, high)

liste = [10, 7, 8, 9, 1, 5]
n = len(liste)
quickSort(liste, 0, n-1)
print(liste)