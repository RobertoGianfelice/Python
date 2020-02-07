stringa=input("Inserisci la stringa da analizzare: ")

sinistra=0
destra=len(stringa)-1
palindromo=True

while (sinistra<destra and palindromo):
    palindromo=stringa[sinistra]==stringa[destra]
    sinistra+=1
    destra-=1

if palindromo:
    print("La stringa è un palindromo")
else:
    print("La stringa non è un palindromo")
