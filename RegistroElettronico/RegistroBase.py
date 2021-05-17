registro={}

############################################
# Questa funzione consente di inserire     #
# il voto di uno studente: se lo studente  #
# non esiste lo aggiunge, altrimenti sovra-#
# scrive il voto presente nel registro     #
############################################
def inserimento():
     print("inserimento")
     nome=input("Inserisci il nome: ")
     voto=input("Inserisci il voto: ")
     registro[nome]=voto
     print(registro)

############################################
# Questa funzione consente di stampare o   #
# tutto il registro o solo uno studente    #
############################################
def stampa():
     print("stampa")


scelta="0"
while(scelta!="3"):
     print("1] Inserimento voti")
     print("2] Stampa registro")
     print("3] Esci")
     scelta=input("Cosa scegli? ")
     if (scelta=="1"):
          inserimento()
     elif (scelta=="2"):
          stampa()
     elif (scelta=="3"):
          print("Bye bye")
     else:
          print("Devi inserire o 1 o 2 o3")
