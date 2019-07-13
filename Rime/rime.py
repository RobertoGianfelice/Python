a=3
b=1
c=1

def rime(a,b,c,metrica):

  l=len(metrica)
  if len(metrica)==5:
    print("metrica=",metrica)
  else:
    if a>0:
      rime(a-1,b,c,metrica+"a")

    if b>0 and l>=1:
      rime(a,b-1,c,metrica+"b")

    if c>0 and l>=2:
      rime(a,b,c-1,metrica+"c")

rime(3,1,1,"")
