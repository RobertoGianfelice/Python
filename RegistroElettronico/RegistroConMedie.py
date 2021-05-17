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
     if (nome in registro):
          registro[nome].append(voto)
     else:
          registro[nome]=[voto]

     #registro[nome]=voto
     print(registro)

############################################
# Questa funzione consente di cancellare   #
# i voto di uno studente                   #
############################################
def cancellaVoti():
     print("cancellaVoti")
     nome=input("Inserisci il nome: ")
     if (nome in registro):
          registro.pop(nome)
          print(nome, " è stato tolto dal registro")
     else:
          print(nome, " Non è presente nel registro")

     #registro[nome]=voto
     print(registro)



############################################
# Questa funzione consente di stampare o   #
# tutto il registro o solo uno studente    #
############################################
def stampa():
     print("stampa")
     for nome in registro.keys():
          print (nome, "ha questi voti: ",end="")
          for voto in registro[nome]:
               print(voto, end=" ")
          print()
############################################
# Questa funzione consente di calcolare    #
# la media dei valori di una lista di carat#
# teri                                     #
############################################
def mediaDellaLista(lista):
     somma=0
     for voto in lista:
          votoNumerico=int(voto)
          somma=somma+votoNumerico
     return(somma/lista.len)


############################################
# Questa funzione consente di stampare la  #
# media dei voti per ogni studente presente#
# nel registro                             #
############################################
def CalcolaMedie():
     print("CalcolaMedie")
     while(scelta!="4"):
          print("1] Media per tutti i singoli studenti")
          print("2] Media per singolo studente")
          print("3] Media della classe")
          print("4] Ritorna la menu principale")
          scelta=input("Cosa scegli? ")


scelta="0"
while(scelta!="5"):
     print("1] Inserimento voti")
     print("2] Cancella voti")
     print("3] Stampa registro")
     print("4] Calcola medie")
     print("5] Esci")
     scelta=input("Cosa scegli? ")
     if (scelta=="1"):
          inserimento()
     elif (scelta=="2"):
          cancellaVoti()
     elif (scelta=="3"):
          stampa()
     elif (scelta=="4"):
          calcolaMedie()
     elif (scelta=="5"):
          print("Ultimo giro")
     else:
          print("Devi inserire o 1 o 2 o 3 o 4")

print("Programma terminato")
