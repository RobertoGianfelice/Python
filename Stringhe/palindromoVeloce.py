stringa=input("Inserisci la stringa da analizzare:")
print(stringa[0:len(stringa):2])
if (stringa==stringa[::-1]):
    print("La stringa è palindroma")
else:
    print("La stringa non è palindroma")
