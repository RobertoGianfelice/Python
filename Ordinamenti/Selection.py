import random

numeri=[]
n=10

for i in range(n):
    numeri.append(i)
random.shuffle(numeri)

print(numeri)

for i in range(n-1):
    for j in range(i+1,n):
        if (numeri[i]>numeri[j]):
            temp=numeri[i]
            numeri[i]=numeri[j]
            numeri[j]=temp
    print(f"{numeri} ordinato fino a {i+1}")

print(f"Finito {numeri}")
