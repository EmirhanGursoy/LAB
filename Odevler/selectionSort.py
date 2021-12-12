import sys
Liste = [64, 25, 12, 22, 11]
  
for i in range(len(Liste)):
    min_idx = i
    for j in range(i+1, len(Liste)):
        if Liste[min_idx] > Liste[j]:
            min_idx = j                     
    Liste[i], Liste[min_idx] = Liste[min_idx], Liste[i]
  

print(Liste)