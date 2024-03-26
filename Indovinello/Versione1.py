from itertools import permutations 
  
def testa(lista):
    up=[1,3,5,7,9,11]
    for i in up:
        if lista[i] != (lista[i-1]+lista[i+1]):
            return False
    return True

# Get all permutations of [1, 2, 3] 
perm = permutations([1, 2, 3,4,5,6,7,8,9,10,11,12,13]) 

# Print the obtained permutations 
for i in list(perm): 
    if testa(i):
        print(f"Trovata soluzione: {i}") 
