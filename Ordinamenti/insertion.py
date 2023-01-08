import random

numeri=[]
n=10

for i in range(n):
    numeri.append(i)
random.shuffle(numeri)

#print(numeri)

for i in range(1,n):
    for j in range(i):
        if (numeri[i]<numeri[j]):
            temp=numeri[i]
            numeri[i]=numeri[j]
            numeri[j]=temp
    print(f"{numeri} ordinato fino a {i}")

print(f"Finito {numeri}")
