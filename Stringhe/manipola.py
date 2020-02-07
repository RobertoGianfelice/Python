nome=input("Per favore inserisci il tuo nome: ")

print("Il valore inserito e': ",nome)

carattere=int(input("Quale carattere vuoi stampare? "))

if (carattere <= len(nome)):
    print("Il carattere vale", nome[carattere-1])
else:
    print("Il nome ", nome, "ha al massimo ", len(nome), "caratteri")

for c in nome:
    print(c)

