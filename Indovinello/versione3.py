import datetime
""" Salvo l'ora di inizio elaborazione"""
inizio = datetime.datetime.now()
""" Contatore combinazioni"""
i = 0

numeroGettoni=int(input("Inserisci il numero di gettoni (max 21): "))
l0=[]
for n in range(1, numeroGettoni+1):
    l0.append(n)
pari=0
dispari=0

""" Accetto le permutazioni di lunghezza dispari con l'ultima terna 
    che rispetta le regole. Scarto le altre """
def checkDispari(l):
    global pari
    pari+=1
    return( l[1] == l[0]+l[2])

""" Accetto le permutazioni di lunghezza pari con l'ultimo elemento 
    (quello in alto, maggiore del penultimo (quello in basso).
    Scarto le altre """
def checkPari(l):
    global dispari
    dispari +=1
    return (l[1] > l[0])

""" Stampa formattata della soluzione ottenuta"""
def stampaSoluzione(soluzione):
    global i
    i+=1
    dSpace="    "
    print(f"\n{i}:")
    print(f"{dSpace}",end="")
    lSoluzione=len(soluzione)
    for j in range(1,lSoluzione,2):
        print(f"{soluzione[j]:3}{dSpace}", end="")
    print()
    for j in range(0,lSoluzione,2):
        print(f"{soluzione[j]:3}{dSpace}", end="")
    print()

""" Ogni ciclo gestisce l'i-esimo elemento della permutazione. Quando lo propone
    viene verificata (con la funzione check pari e check dispari a seconda 
    della lunghezza della combinazione che si sta formando) l'accettabilità 
    della combinazione scartando ciò che sicuramente non rispetta le regole del 
    gioco."""
for i0 in range(len(l0)):
    if (i0 == max(l0)):
        continue
    l1 = l0[:]
    l1.pop(i0)
    for i1 in range(len(l1)):
        if not (checkPari([l0[i0], l1[i1]])):
            continue
        l2 = l1[:]
        l2.pop(i1)
        for i2 in range(len(l2)):
            """ verifica accettabilità con i2. Se non accettabile, scarta il resto di tutte le
             permutazioni con i2 in quella posizione abbattendo così la complessità totale.
             Stesso approccio per tutte le posizioni dispari"""
            if not (checkDispari([l0[i0], l1[i1], l2[i2]])):
                continue
            l3 = l2[:]
            if (len(l3)==1):
                soluzione=[l0[i0],l1[i1],l2[i2]]
                stampaSoluzione(soluzione)
                break
            l3.pop(i2)
            for i3 in range(len(l3)):
                """ verifica accettabilità con i3. Se non accettabile, scarta il resto di tutte le
                permutazioni con i3 in quella posizione abbattendo così la complessità totale.
                Stesso approccio per tutte le posizioni pari"""
                if not (checkPari([l2[i2], l3[i3]])):
                    continue
                l4 = l3[:]
                l4.pop(i3)
                for i4 in range(len(l4)):
                    if not (checkDispari([l2[i2], l3[i3], l4[i4]])):
                        continue
                    l5 = l4[:]
                    if (len(l5)==1):
                        soluzione=[l0[i0],l1[i1],l2[i2],l3[i3],l4[i4]]
                        stampaSoluzione(soluzione)
                        break
                    l5.pop(i4)
                    for i5 in range(len(l5)):
                        if not (checkPari([l4[i4], l5[i5]])):
                            continue
                        l6 = l5[:]
                        l6.pop(i5)
                        for i6 in range(len(l6)):
                            if not (checkDispari([l4[i4], l5[i5], l6[i6]])):
                                continue
                            l7 = l6[:]
                            if (len(l7)==1):
                                soluzione=[l0[i0],l1[i1],l2[i2],l3[i3],l4[i4],l5[i5],l6[i6]]
                                stampaSoluzione(soluzione)
                                break
                            l7.pop(i6)
                            for i7 in range(len(l7)):
                                if not (checkPari([l6[i6], l7[i7]])):
                                    continue
                                l8 = l7[:]
                                l8.pop(i7)
                                for i8 in range(len(l8)):
                                    if not (checkDispari([l6[i6], l7[i7], l8[i8]])):
                                        continue
                                    l9 = l8[:]
                                    if (len(l9)==1):
                                        soluzione=[l0[i0],l1[i1],l2[i2],l3[i3],l4[i4],
                                                   l5[i5],l6[i6],l7[i7],l8[i8]]
                                        stampaSoluzione(soluzione)
                                        break
                                    l9.pop(i8)
                                    for i9 in range(len(l9)):
                                        if not (checkPari([l8[i8], l9[i9]])):
                                            continue
                                        l10 = l9[:]
                                        l10.pop(i9)
                                        for i10 in range(len(l10)):
                                            if not (checkDispari([l8[i8], l9[i9], l10[i10]])):
                                                continue
                                            l11 = l10[:]
                                            if (len(l11)==1):
                                                soluzione=[l0[i0],l1[i1],l2[i2],l3[i3],l4[i4],
                                                           l5[i5],l6[i6],l7[i7],l8[i8],l9[i9],
                                                           l10[i10]]
                                                stampaSoluzione(soluzione)
                                                break
                                            l11.pop(i10)
                                            for i11 in range(len(l11)):
                                                if not (checkPari([l10[i10], l11[i11]])):
                                                    continue
                                                l12 = l11[:]
                                                l12.pop(i11)
                                                for i12 in range(len(l12)):
                                                    if not (checkDispari([l10[i10], l11[i11], l12[i12]])):
                                                        continue
                                                    l13 = l12[:]
                                                    if (len(l13)==1):
                                                        soluzione=[l0[i0],l1[i1],l2[i2],l3[i3],l4[i4],
                                                                   l5[i5],l6[i6],l7[i7],l8[i8],l9[i9],
                                                                   l10[i10],l11[i11],l12[i12]]
                                                        stampaSoluzione(soluzione)
                                                        break
                                                    l13.pop(i12)
                                                    for i13 in range(len(l13)):
                                                        if not (checkPari([l12[i12], l13[i13]])):
                                                            continue
                                                        l14 = l13[:]
                                                        l14.pop(i13)
                                                        for i14 in range(len(l14)):
                                                            if not (checkDispari([l12[i12], l13[i13], l14[i14]])):
                                                                continue
                                                            l15 = l14[:]
                                                            if (len(l15)==1):
                                                                soluzione=[l0[i0],l1[i1],l2[i2],l3[i3],l4[i4],
                                                                           l5[i5],l6[i6],l7[i7],l8[i8],l9[i9],
                                                                           l10[i10],l11[i11],l12[i12],l13[i13],
                                                                           l14[i14]]
                                                                stampaSoluzione(soluzione)
                                                                break
                                                            l15.pop(i14)
                                                            for i15 in range(len(l15)):
                                                                if not (checkPari([l14[i14],l15[i15]])):
                                                                    continue
                                                                l16 = l15[:]
                                                                l16.pop(i15)
                                                                for i16 in range(len(l16)):
                                                                    if not (checkDispari([l14[i14],l15[i15],l16[i16]])):
                                                                        continue
                                                                    l17 = l16[:]
                                                                    if (len(l17)==1):
                                                                        soluzione=[l0[i0],l1[i1],l2[i2],l3[i3],l4[i4],
                                                                                   l5[i5],l6[i6],l7[i7],l8[i8],l9[i9],
                                                                                   l10[i10],l11[i11],l12[i12],l13[i13],
                                                                                   l14[i14],l15[i15],l16[i16]]
                                                                        stampaSoluzione(soluzione)
                                                                        break
                                                                    l17.pop(i16)
                                                                    for i17 in range(len(l17)):
                                                                        if not (checkPari([l16[i16],l17[i17]])):
                                                                            continue
                                                                        l18 = l17[:]
                                                                        l18.pop(i17)
                                                                        for i18 in range(len(l18)):
                                                                            if not (checkDispari([l16[i16], l17[i17],l18[i18]])):
                                                                                continue
                                                                            l19 = l18[:]
                                                                            if (len(l19)==1):
                                                                                soluzione=[l0[i0],l1[i1],l2[i2],l3[i3],l4[i4],
                                                                                           l5[i5],l6[i6],l7[i7],l8[i8],l9[i9],
                                                                                           l10[i10],l11[i11],l12[i12],l13[i13],
                                                                                           l14[i14],l15[i15],l16[i16],l17[i17],
                                                                                           l18[i18]]
                                                                                stampaSoluzione(soluzione)
                                                                                break
                                                                            l19.pop(i18)
                                                                            for i19 in range(len(l19)):
                                                                                if not (checkPari([l18[i18], l19[i19]])):
                                                                                    continue
                                                                                l20 = l19[:]
                                                                                l20.pop(i19)
                                                                                if (checkDispari([l18[i18], l19[i19], l20[0]])):
                                                                                    """ La permutazione è una soluzione: incremento il contatore e la stampo!!!"""
                                                                                    soluzione=[l0[i0],l1[i1],l2[i2],l3[i3],l4[i4],
                                                                                               l5[i5],l6[i6],l7[i7],l8[i8],l9[i9],
                                                                                               l10[i10],l11[i11],l12[i12],l13[i13],
                                                                                               l14[i14],l15[i15],l16[i16],l17[i17],
                                                                                               l18[i18],l19[i19],l20[0]]
                                                                                    stampaSoluzione(soluzione)
                                                                                
                                                         

""" Orario fine elaborazione """
fine = datetime.datetime.now()

print(f"Ora inizio={inizio}  Ora fine {fine} \nTempo impiegato {fine-inizio} \n controlli effettuati= {pari+dispari} pari={pari} dispari={dispari}")

