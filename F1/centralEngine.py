import mysql.connector
import os
import time

iscritti=[("Verstappen","VER","RedBull","REB","0:0:0","0:1:0","0:0:0","S",0),
            ("Perez","PER","RedBull","REB","0:0:0","0:2:0","0:0:0","S",0),
            ("Leclerc","LEC","Ferrari","FER","0:0:0","0:3:0","0:0:0","S",0),
            ("Sainz","SAI","Ferrrari","FER","0:0:0","0:4:0","0:0:0","S",0),
            ("Hamilton","HAM","Mercedes","MER","0:0:0","0:5:0","0:0:0","S",0),
            ("Russel","RUS","Mercedes","MER","0:0:0","0:6:0","0:0:0","S",0)]

onGrid=[("VER",100,100,100,100,0),
            ("PER",100,100,100,100,0),
            ("LEC",100,100,100,100,0),
            ("SAI",100,100,100,100,0),
            ("HAM",100,100,100,100,0),
            ("RUS",100,100,100,100,0)]
def setupPiloti():
    mydb = mysql.connector.connect(
      host="localhost",
      user="F1",
      password="F1",
      database="F1"
    )
    print(iscritti)

    mycursor = mydb.cursor()
    sql = "INSERT INTO Piloti (nome, nick, macchina, nickCar, tTot, tLastLap, gap,tyre, LapOnTyre) \
                        VALUES (%s, %s,  %s,  %s,  %s,  %s,  %s, %s, %s)"

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
    sql = "INSERT INTO muretto (nickPilota, perfOnLap, resaGomme, fuel, powerOnLap, boxboxbox)  \
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
    mycursor = mydb.cursor()
    mycursor.execute("update piloti set tTot=addtime(tTot,tLastLap),tLastLap=%s, gap=timediff(tTot,%s)",parameters)
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
    mycursor.execute("select nick,nickCar,tTot,tLastLap,gap from Piloti order by tTot")
    myresult = mycursor.fetchall()
    print(f"Driver\tCar\ttTot\t\tLastLap\t\tGap")

    for x in myresult:
        print(f"{x[0]}\t{x[1]}\t{x[2]}\t\t{x[3]}\t\t{x[4]}")
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
    for j in range(5):
        time.sleep(1)
        print(".")
    leadTime=str(getLeadTime())
    print(leadTime)
    time.sleep(2)
    aggiornaTempi(["0:1:0",leadTime])
