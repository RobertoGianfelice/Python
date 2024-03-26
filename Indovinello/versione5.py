import datetime
""" Salvo l'ora di inizio elaborazione"""
inizio = datetime.datetime.now()
""" Contatore combinazioni"""
i = 0

numeroGettoni=int(input("Inserisci il numero di gettoni (max 23): "))
l0=[]
for n in range(1, numeroGettoni+1):
    l0.append(n)
pari=0
scartoPari=0
scartoDispari=0



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
        scartoDispari+=1
        continue
    l1 = l0[:]
    l1.pop(i0)
    for i1 in range(len(l1)):
        """ Accetto le permutazioni di lunghezza pari con l'ultimo elemento 
        (quello in alto, maggiore del penultimo (quello in basso).
        Scarto le altre """
        if (l0[i0] > l1[i1]):
            scartoPari+=1
            continue
        l2 = l1[:]
        l2.pop(i1)
        """ verifica esistenza del terzo elemento. Se non esiste, scarta il resto di tutte le
        permutazioni con l2[i2] in quella posizione abbattendo così la complessità totale.
        Stesso approccio per tutte le posizioni che completano la terna"""
        if ((l1[i1]-l0[i0]) not in l2): 
            scartoDispari+=1
            continue
        """ calcola il completamento della terna"""
        i2=l2.index(l1[i1]-l0[i0])
        l3 = l2[:]
        if (len(l3)==1):
            soluzione=[l0[i0],l1[i1],l2[i2]]
            stampaSoluzione(soluzione)
            break
        l3.pop(i2)
        for i3 in range(len(l3)):
            """ verifica accettabilità con l3[i3] (posizioni in alto): il nuovo elmento deve 
            essere minore del precedente. Se non accettabile, scarta il resto di tutte le permutazioni 
            con l3[i3] in quella posizione abbattendo così la complessità totale. 
            Stesso approccio per tutte le posizioni in alto"""
            if (l2[i2] > l3[i3]):
                scartoPari+=1
                continue
            l4 = l3[:]
            l4.pop(i3)
            if ((l3[i3]-l2[i2]) not in l4): 
                scartoDispari+=1
                continue
            i4=l4.index(l3[i3]-l2[i2])
            l5 = l4[:]
            if (len(l5)==1):
                soluzione=[l0[i0],l1[i1],l2[i2],l3[i3],l4[i4]]
                stampaSoluzione(soluzione)
                break
            l5.pop(i4)
            for i5 in range(len(l5)):
                if (l4[i4]>l5[i5]):
                    scartoPari+=1
                    continue
                l6 = l5[:]
                l6.pop(i5)
                if ((l5[i5]-l4[i4]) not in l6): 
                    scartoDispari+=1
                    continue
                i6=l6.index(l5[i5]-l4[i4])
                l7 = l6[:]
                if (len(l7)==1):
                    soluzione=[l0[i0],l1[i1],l2[i2],l3[i3],l4[i4],l5[i5],l6[i6]]
                    stampaSoluzione(soluzione)
                    break
                l7.pop(i6)
                for i7 in range(len(l7)):
                    if (l6[i6]>l7[i7]):
                        scartoPari+=1
                        continue
                    l8 = l7[:]
                    l8.pop(i7)
                    if ((l7[i7]-l6[i6]) not in l8): 
                        scartoDispari+=1
                        continue
                    i8=l8.index(l7[i7]-l6[i6])
                    l9 = l8[:]
                    if (len(l9)==1):
                        soluzione=[l0[i0],l1[i1],l2[i2],l3[i3],l4[i4],
                                    l5[i5],l6[i6],l7[i7],l8[i8]]
                        stampaSoluzione(soluzione)
                        break
                    l9.pop(i8)
                    for i9 in range(len(l9)):
                        if (l8[i8]>l9[i9]):
                            scartoPari+=1
                            continue
                        l10 = l9[:]
                        l10.pop(i9)
                        if ((l9[i9]-l8[i8]) not in l10): 
                            scartoDispari+=1
                            continue
                        i10=l10.index(l9[i9]-l8[i8])
                        l11 = l10[:]
                        if (len(l11)==1):
                            soluzione=[l0[i0],l1[i1],l2[i2],l3[i3],l4[i4],
                                        l5[i5],l6[i6],l7[i7],l8[i8],l9[i9],
                                        l10[i10]]
                            stampaSoluzione(soluzione)
                            break
                        l11.pop(i10)
                        for i11 in range(len(l11)):
                            if (l10[i10]>l11[i11]):
                                scartoPari+=1
                                continue
                            l12 = l11[:]
                            l12.pop(i11)
                            if ((l11[i11]-l10[i10]) not in l12): 
                                scartoDispari+=1
                                continue
                            i12=l12.index(l11[i11]-l10[i10])
                            l13 = l12[:]
                            if (len(l13)==1):
                                soluzione=[l0[i0],l1[i1],l2[i2],l3[i3],l4[i4],
                                            l5[i5],l6[i6],l7[i7],l8[i8],l9[i9],
                                            l10[i10],l11[i11],l12[i12]]
                                stampaSoluzione(soluzione)
                                break
                            l13.pop(i12)
                            for i13 in range(len(l13)):
                                if (l12[i12]>l13[i13]):
                                    scartoPari+=1
                                    continue
                                l14 = l13[:]
                                l14.pop(i13)
                                if ((l13[i13]-l12[i12]) not in l14): 
                                    scartoDispari+=1
                                    continue
                                i14=l14.index(l13[i13]-l12[i12])
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
                                    if (l14[i14]>l15[i15]):
                                        scartoPari+=1
                                        continue
                                    l16 = l15[:]
                                    l16.pop(i15)
                                    if ((l15[i15]-l14[i14]) not in l16): 
                                        scartoDispari+=1
                                        continue
                                    i16=l16.index(l15[i15]-l14[i14])
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
                                        if (l16[i16]>l17[i17]):
                                            scartoPari+=1
                                            continue
                                        l18 = l17[:]
                                        l18.pop(i17)
                                        if ((l17[i17]-l16[i16]) not in l18): 
                                            scartoDispari+=1
                                            continue
                                        i18=l18.index(l17[i17]-l16[i16])
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
                                            if (l18[i18]>l19[i19]):                                                
                                                scartoPari+=1
                                                continue
                                            l20 = l19[:]
                                            l20.pop(i19)
                                            if ((l19[i19]-l18[i18]) not in l20): 
                                                scartoDispari+=1
                                                continue
                                            i20=l20.index(l19[i19]-l18[i18])
                                            l21 = l20[:]
                                            if (len(l21)==1):
                                                soluzione=[l0[i0],l1[i1],l2[i2],l3[i3],l4[i4],
                                                            l5[i5],l6[i6],l7[i7],l8[i8],l9[i9],
                                                            l10[i10],l11[i11],l12[i12],l13[i13],
                                                            l14[i14],l15[i15],l16[i16],l17[i17],
                                                            l18[i18],l19[i19],l20[i20]]
                                                stampaSoluzione(soluzione)
                                                break

                                            l21.pop(i20)
                                            for i21 in range(len(l21)):
                                                if (l20[i20]>l21[i21]):
                                                    scartoPari+=1
                                                    continue
                                                l22 = l21[:]
                                                l22.pop(i21)
                                                if (l21[i21]==l20[i20]+l22[0]):
                                                    """ La permutazione è una soluzione: incremento il contatore e la stampo!!!"""
                                                    soluzione=[l0[i0],l1[i1],l2[i2],l3[i3],l4[i4],
                                                                l5[i5],l6[i6],l7[i7],l8[i8],l9[i9],
                                                                l10[i10],l11[i11],l12[i12],l13[i13],
                                                                l14[i14],l15[i15],l16[i16],l17[i17],
                                                                l18[i18],l19[i19],l20[i20],l21[i21],
                                                                l22[0]]
                                                    stampaSoluzione(soluzione)
                                            
                                              

""" Orario fine elaborazione """
fine = datetime.datetime.now()

print(f"Ora inizio={inizio}  Ora fine {fine} \nTempo impiegato {fine-inizio} \n taglie effettuati pari={scartoPari} dispari={scartoDispari}")

