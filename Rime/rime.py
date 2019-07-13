totale=0
def rime(lettere,n,m,metrica):
  global totale
  l=len(metrica)
  completo=True
  somma=0
  for i in range(m):
    completo=lettere[i]>0 and completo
    somma+=lettere[i]

  if l==n and completo:
    totale+=1
    print("metrica[",totale,"]=",metrica)
  else:
    for i in range(m):
      if somma<=n and lettere[i]<=n-m+1 and l>=i and (i==0 or lettere[i-1]>0):
        lettere2=lettere[:]
        lettere2[i]+=1
        rime(lettere2,n,m,metrica+chr(ord("a")+i))

#Main
n=int(input("Inserisci la lunghezza della sequenza: "))
m=n+1
while (m>n or m<1):
  m=int(input("Inserisci il numero di rime: "))

lettere=[]
for i in range(m):
  lettere.append(0)
rime(lettere,n,m,"")
