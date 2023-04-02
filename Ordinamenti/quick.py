from random import randint
n=10
numeri=[]
for i in range(n):
    numeri.append(randint(1,100))
print(numeri)

def quickSort(vettore,s,d):
    if (s<d):
        q=partiziona(vettore,s,d)
        quickSort(vettore, s, q-1)
        quickSort(vettore, q+1, d)

def partiziona(v,s,d):
    ipivot=s
    pivot=v[ipivot]
    while(s<d):
        while(v[s] <= pivot and s<d):
            s+=1
        while (v[d] > pivot):
            d-=1
        if (s<d):
            v[s],v[d]=v[d],v[s]
    v[ipivot],v[d]=v[d],v[ipivot]
    return d

quickSort(numeri, 0, len(numeri)-1)
print(f"Il vettore ordinato è {numeri}")
