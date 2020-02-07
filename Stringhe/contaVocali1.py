stringa=input("Per favore inserisci una stringa: ")

print("Il valore inserito e': ",stringa)

conta_a=conta_e=conta_i=conta_o=conta_u=0

for c in stringa:
    if (c=="a"):
        conta_a+=1
    elif (c=="e"):
        conta_e+=1
    elif (c=="i"):
        conta_+=1
    elif (c=="o"):
        conta_o+=1
    elif (c=="u"):
        conta_u+=1
        
max_vocale="a"
max_value=conta_a
if (conta_e > max_value):
    max_vocale="e"
    max_value=conta_e
if (conta_i > max_value):
    max_vocale="i"
    max_value=conta_i
if (conta_o > max_value):
    max_vocale="o"
    max_value=conta_o
if (conta_u > max_value):
    max_vocale="u"
    max_value=conta_u
print ("La vocale più ripetuta è la '" + max_vocale + "'. Si ripete", max_value, "volte")





