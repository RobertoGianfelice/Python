l0 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
    12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
pari=0
dispari=0

def checkDispari(l):
    global pari
    pari+=1
    return( l[1] == l[0]+l[2])
def checkPari(l):
    global dispari
    dispari +=1
    return (l[len(l)-1] > l[len(l)-2])



i = 0
for i0 in range(len(l0)):
    l1 = l0[:]
    l1.pop(i0)
    for i1 in range(len(l1)):
        l2 = l1[:]
        l2.pop(i1)
        for i2 in range(len(l2)):
            if not (checkDispari([l0[i0], l1[i1], l2[i2]])):
                continue
            l3 = l2[:]
            l3.pop(i2)
            for i3 in range(len(l3)):
                if not (checkPari([l1[i1], l2[i2], l3[i3]])):
                    continue
                l4 = l3[:]
                l4.pop(i3)
                for i4 in range(len(l4)):
                    if not (checkDispari([l2[i2], l3[i3], l4[i4]])):
                        continue
                    l5 = l4[:]
                    l5.pop(i4)
                    for i5 in range(len(l5)):
                        if not (checkPari([l3[i3] ,l4[i4], l5[i5]])):
                            continue
                        l6 = l5[:]
                        l6.pop(i5)
                        for i6 in range(len(l6)):
                            if not (checkDispari([l4[i4], l5[i5], l6[i6]])):
                                continue
                            l7 = l6[:]
                            l7.pop(i6)
                            for i7 in range(len(l7)):
                                if not (checkPari([l5[i5], l6[i6], l7[i7]])):
                                    continue
                                l8 = l7[:]
                                l8.pop(i7)
                                for i8 in range(len(l8)):
                                    if not (checkDispari([l6[i6], l7[i7], l8[i8]])):
                                        continue
                                    l9 = l8[:]
                                    l9.pop(i8)
                                    for i9 in range(len(l9)):
                                        if not (checkPari([l7[i7], l8[i8], l9[i9]])):
                                            continue
                                        l10 = l9[:]
                                        l10.pop(i9)
                                        for i10 in range(len(l10)):
                                            if not (checkDispari([l8[i8], l9[i9], l10[i10]])):
                                                continue
                                            l11 = l10[:]
                                            l11.pop(i10)
                                            for i11 in range(len(l11)):
                                                if not (checkPari([l9[i9], l10[i10], l11[i11]])):
                                                    continue
                                                l12 = l11[:]
                                                l12.pop(i11)
                                                for i12 in range(len(l12)):
                                                    if not (checkDispari([l10[i10], l11[i11], l12[i12]])):
                                                        continue
                                                    l13 = l12[:]
                                                    l13.pop(i12)
                                                    for i13 in range(len(l13)):
                                                        if not (checkPari([ l11[i11], l12[i12], l13[i13]])):
                                                            continue
                                                        l14 = l13[:]
                                                        l14.pop(i13)
                                                        for i14 in range(len(l14)):
                                                            if not (checkDispari([l12[i12], l13[i13], l14[i14]])):
                                                                continue
                                                            l15 = l14[:]
                                                            l15.pop(i14)
                                                            for i15 in range(len(l15)):
                                                                if not (checkPari([l13[i13], l14[i14],l15[i15]])):
                                                                    continue
                                                                l16 = l15[:]
                                                                l16.pop(i15)
                                                                for i16 in range(len(l16)):
                                                                    if not (checkDispari([l14[i14],l15[i15],l16[i16]])):
                                                                        continue
                                                                    l17 = l16[:]
                                                                    l17.pop(
                                                                        i16)
                                                                    for i17 in range(len(l17)):
                                                                        if not (checkPari([l15[i15],l16[i16],l17[i17]])):
                                                                            continue
                                                                        l18 = l17[:]
                                                                        l18.pop(
                                                                            i17)
                                                                        for i18 in range(len(l18)):
                                                                            if not (checkDispari([l16[i16], l17[i17],l18[i18]])):
                                                                                continue
                                                                            l19 = l18[:]
                                                                            l19.pop(
                                                                                i18)
                                                                            for i19 in range(len(l19)):
                                                                                if not (checkPari([l17[i17], l18[i18], l19[i19]])):
                                                                                    continue
                                                                                l20 = l19[:]
                                                                                l20.pop(i19)
                                                                                if (checkDispari([l18[i18], l19[i19], l20[0] ])):
                                                                                    i += 1
                                                                                    print(f"{i}: {l1[i1]:6d} {l3[i3]:4d} {l5[i5]:4d} {l7[i7]:4d} {l9[i9]:4d} {l11[i11]:4d} {l13[i13]:4d} {l15[i15]:4d} {l17[i17]:4d} {l19[i19]:4d}")
                                                                                    print(f"     {l0[i0]:4d} {l2[i2]:4d} {l4[i4]:4d} {l6[i6]:4d} {l8[i8]:4d} {l10[i10]:4d} {l12[i12]:4d} {l14[i14]:4d} {l16[i16]:4d} {l18[i18]:4d} {l20[0]:4d}")
print(f"pari={pari} dispari={dispari}")

