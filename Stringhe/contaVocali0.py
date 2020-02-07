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
        
if (conta_a>conta_e and
    conta_a>conta_i and
    conta_a>conta_o and
    conta_a>conta_u):
    print ("La vocale più ripetuta è la 'a'")
elif (conta_e>conta_a and
    conta_e>conta_i and
    conta_e>conta_o and
    conta_e>conta_u):
    print ("La vocale più ripetuta è la 'e'")
elif (conta_i>conta_a and
    conta_i>conta_e and
    conta_i>conta_o and
    conta_i>conta_u):
    print ("La vocale più ripetuta è la 'i'")
elif (conta_o>conta_a and
    conta_o>conta_e and
    conta_o>conta_i and
    conta_o>conta_u):
    print ("La vocale più ripetuta è la 'o'")
elif (conta_u>conta_a and
    conta_u>conta_e and
    conta_u>conta_i and
    conta_u>conta_o):
    print ("La vocale più ripetuta è la 'u'")

