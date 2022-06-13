n=int(input("Inserire il numero: "))

def stampaNumero(numero):
    print(f"il numero inserito vale {numero}!")

def stampaTabellina(ilNumero):
    for i in range(1,11):
        print(f"{ilNumero}*{i}=\t{ilNumero*i}")

def calcolaPotenza(numero,e):
    pot=numero
    for i in range(1,e+1):
        pot=pot*pot
    return pot

def stampaFattoriale(n):
    fat=n
    for i in range(2,n):
        fat=fat*i
    print(f"Il fattoriale di {n} e' {fat}")


def calcolaFattoriale(numero):
    if numero ==1:
        return 1
    return numero*calcolaFattoriale(numero-1)

stampaNumero(n)
stampaTabellina(n)
esponente=int(input("  Inserisci l'esponente: "))
potenza=calcolaPotenza(n,esponente)
stampaFattoriale(n)

fattoriale=calcolaFattoriale(n)
print(f"Il fattoriale ricorsivo di {n} e' {fattoriale}")
