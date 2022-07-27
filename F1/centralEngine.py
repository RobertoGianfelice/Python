import mysql.connector
import os
import time
import random
tBoxTime="0:0:24"
tLapTime="0:1:0"

iscritti=[["Verstappen","VER","RedBull",    "REB","0:0:0","0:0:0","0:0:0","S",0,"On Race"],
            ["Perez",   "PER","RedBull",    "REB","0:0:0","0:0:0","0:0:0","S",0,"On Race"],
            ["Leclerc", "LEC","Ferrari",    "FER","0:0:0","0:0:0","0:0:0","S",0,"On Race"],
            ["Sainz",   "SAI","Ferrrari",   "FER","0:0:0","0:0:0","0:0:0","S",0,"On Race"],
            ["Hamilton","HAM","Mercedes",   "MER","0:0:0","0:0:0","0:0:0","S",0,"On Race"],
            ["Russel",  "RUS","Mercedes",   "MER","0:0:0","0:0:0","0:0:0","S",0,"On Race"]]

onGrid=[("VER",100,100,100,50,0),
            ("PER",100,100,100,50,0),
            ("LEC",100,100,100,50,0),
            ("SAI",100,100,100,50,0),
            ("HAM",100,100,100,50,0),
            ("RUS",100,100,100,50,0)]
def setupPiloti():
    mydb = mysql.connector.connect(
      host="localhost",
      user="F1",
      password="F1",
      database="F1"
    )
    print(iscritti)

    mycursor = mydb.cursor()
    sql = "INSERT INTO Piloti (nome, nick, macchina, nickCar, tTot, tLastLap, gap,tyre, LapOnTyre, Status) \
                        VALUES (%s, %s,  %s,  %s,  %s,  %s,  %s, %s, %s, %s)"

    random.shuffle(iscritti)
    gap=0
    for iscritto in iscritti:
        iscritto[4]="0:0:" + str(gap)
        gap+=1

    mycursor.executemany(sql, iscritti)
    mydb.commit()

def setupGrid():
    mydb = mysql.connector.connect(
      host="localhost",
      user="F1",
      password="F1",
      database="F1"
    )
    
    print(iscritti)

    mycursor = mydb.cursor()
    sql = "INSERT INTO muretto (nickPilota, throttle, resaGomme, fuel, powerOnLap, boxboxbox)  \
                        VALUES (%s, %s,  %s,  %s,  %s,  %s)"

    mycursor.executemany(sql, onGrid)
    mydb.commit()

def resetGara():
    mydb = mysql.connector.connect(
      host="localhost",
      user="F1",
      password="F1",
      database="F1"
    )

    mycursor = mydb.cursor()
    sql = "delete from Piloti"
    mycursor.execute(sql)
    sql = "delete from muretto"
    mycursor.execute(sql)

    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")

def aggiornaTempi(parameters):
    mydb = mysql.connector.connect(
      host="localhost",
      user="F1",
      password="F1",
      database="F1"
    )
    mycursorSelect = mydb.cursor()
    mycursorUpdate = mydb.cursor()
    mycursorSelect.execute("select nickPilota,throttle,resaGomme,fuel,powerOnLap,boxboxbox \
                            from muretto")
    myresult = mycursorSelect.fetchall()
    mycursorSelect.close()

    for statusCar in myresult:
        tEntrataBox="0:0:0"
        newLapOnTyre=1
        if (statusCar[5]) : #la macchina è stata richiamata per cambio gomme
            tEntrataBox=tBoxTime
            newLapOnTyre=0

        if (statusCar[3]>0):
            localParameters=[parameters[1],tEntrataBox,parameters[0],statusCar[4],newLapOnTyre,statusCar[0]]
            print(localParameters)

            mycursorUpdate.execute("update piloti set gap=timediff(tTot,%s),\
                                            tTot=addtime(addtime(tTot,tLastLap),%s),\
                                            tLastLap=sec_to_time(time_to_sec(%s)+(1-(%s/100))*100),\
                                            LapOnTyre=LapOnTyre*%s+1\
                            where nick=%s",localParameters) #usa nickname
        else:
            mycursorUpdate.execute("update piloti set status='OUT'\
                            where nick=%s",[statusCar[0]]) #usa nickname
    mycursorUpdate.close()
    mydb.commit()


def updateCarPerformance():
    mydb = mysql.connector.connect(
      host="localhost",
      user="F1",
      password="F1",
      database="F1"
    )

    mycursorSelect = mydb.cursor()

    mycursorSelect.execute("select nickPilota,throttle,resaGomme,fuel,powerOnLap,boxboxbox \
                            from muretto")
    myresult = mycursorSelect.fetchall()
    mycursorSelect.close()

    for statusCar in myresult:
        mycursorUpdate = mydb.cursor()

        tEntrataBox="0:0:0"
        newResaGomme=statusCar[2]-statusCar[1]/50
        newpowerOnLap=statusCar[1]-(1-newResaGomme/100)*100
        if (statusCar[5]):
            tEntrataBox=tBoxTime
            newResaGomme=100

        localParameters=[newResaGomme,newpowerOnLap,statusCar[0]]
        mycursorUpdate.execute("update muretto set resaGomme=%s,\
                                                fuel=fuel-throttle/100,\
                                                powerOnLap=%s, \
                                                boxboxbox=0 \
                            where nickPilota=%s",localParameters) #usa nickname
        mycursorUpdate.close()
    mydb.commit()

    mycursorUpdate = mydb.cursor()

    mycursorUpdate.close()
    mydb.commit()


def stampaClassifica(lap):
    mydb = mysql.connector.connect(
      host="localhost",
      user="F1",
      password="F1",
      database="F1"
    )
    mycursor = mydb.cursor()
    os.system('clear')
    print(f"------------- LAP {lap} ---------------")
    mycursor.execute("select nick,nickCar,tTot,tLastLap,gap, LapOnTyre, resaGomme, powerOnLap, status \
                      from Piloti, muretto \
                      where nick=nickPilota \
                      order by status,tTot")
    myresult = mycursor.fetchall()
    print(f"Driver\tCar\ttTot\t\tLastLap\t\tGap\tLapOnTyre\tresaGomme\t powerOnLap \t Status")

    for x in myresult:
        if x[8]!="Out":
            print(f"{x[0]}\t{x[1]}\t{x[2]}\t\t{x[3]}\t\t{x[4]}\t\t{x[5]}\t{x[6]}\t\t{x[7]}\t{x[8]}")
        else:
            print(f"{x[0]}\t{x[1]}\t\t OUT")
    mycursor.close()

def getLeadTime():
    mydb = mysql.connector.connect(
      host="localhost",
      user="F1",
      password="F1",
      database="F1"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT tTot FROM Piloti order by tTot")
    myresult = mycursor.fetchone()
    return (myresult[0])

print("Resetting race")
resetGara()
print("Loading new race")
setupPiloti()
setupGrid()

for i in range(40):
    stampaClassifica(i)
    for j in range(3):
        time.sleep(1)
        print(".")
    leadTime=str(getLeadTime())
    time.sleep(2)
    aggiornaTempi([tLapTime,leadTime])
    updateCarPerformance()


stampaClassifica(40)
