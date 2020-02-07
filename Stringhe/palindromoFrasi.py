##Ero a dirottar trattori da ore
##Ai lati d’Italia
##I seni cinesi
##Etna gigante
##Era pacifica pare
##I brevi diverbi
##
##https://www.frasimania.it/frasi-palindrome/


stringa=input("Inserisci la stringa da analizzare: ")
stringa=stringa.lower()
sinistra=0
destra=len(stringa)-1
palindromo=True

while (sinistra<destra and palindromo):
    if (stringa[sinistra] in " ',’" ):
        print("salto <" + stringa[sinistra] + ">")
        sinistra+=1
    elif (stringa[destra] in " ',’"):
        print("salto " + stringa[destra])
        destra-=1
    else:
        palindromo=stringa[sinistra]==stringa[destra]
        print("confronto " +stringa[sinistra] + " e "+stringa[destra])
        sinistra+=1
        destra-=1

if palindromo:
    print("La stringa è un palindromo")
else:
    print("La stringa non è un palindromo")
