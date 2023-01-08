n=int(input(f"inserisci il numero: "))

def fattorialeRic1(n):
    if n==0:
        return 1
    else: 
        return n*fattoriale(n-1)

def fattorialeRic2(n,fatt,iterazione):
    if (iterazione<=n):
        fatt=fatt*iterazione
        iterazione+=1
        return(fattorialeRic2(n, fatt, iterazione))
    return fatt

def fattorialeIterativo(n):
    fatt=1
    for i in range(1,n+1):
        fatt=fatt*i
    return(fatt)

def fibonacci(n):
    if n>2:
        return fibonacci(n-1)+fibonacci(n-2)
    else:
        return 1

def fibonacciIterativo(n):
    a=1
    b=1
    for i in range(n):
        c=b
        b=a+b
        a=c
    return(b)
    

print(f"Il fattoriale di {n} è {fattorialeRic2(n, 1, 1)}")
print(f"il numero {n} della successione di Fibonacci è {fibonacciIterativo(n)}")