import sqlite3 as lite

conn = None

def initDB():

    conn = lite.connect("base.db")              #connection à la base
    #DONNEES TABLE 1
    table1 = (
        ('paul','bidule','m1informatique','1996-10-28','rue albert camus',32,'angers'),
        ('michel','rodriguez','m2pro','1965-02-06','avenue des champs élysées',2,'paris'),
        ('alain','proviste','m2pro','1932-02-18','avenue des champs élysées',8,'paris'),
        ('jean','de la fontaine','ecole des poetes','1568-12-03','sous la fontaine',6,'avignon')
    )
    #DONNEES TABLE 2
    table2 = (
        ('garcia','enseignant','m1informatique'),
        ('barichard','enseignant_responsable','m2pro'),
        ('damotta','enseignant','m1informatique')
    )


    #CREATION ET INSERTION DANS LES TABLES
    with conn:
        cursor = conn.cursor()                      #le cursor
        
        #creation, insertion table1
        cursor.execute("DROP TABLE IF EXISTS table1")
        cursor.execute("CREATE TABLE table1(prenom VARCHAR(20), nom VARCHAR(20),diplome VARCHAR(50),ddn date,rue VARCHAR(50), numero INT, ville VARCHAR(30))")
        cursor.executemany("INSERT INTO table1 VALUES(?,?,?,?,?,?,?)",table1)
        
            #creation, insertion table2
        cursor.execute("DROP TABLE IF EXISTS table2")
        cursor.execute("CREATE TABLE table2(responsable VARCHAR(20),fonction VARCHAR(30),diplome VARCHAR(20))")
        cursor.executemany("INSERT INTO table2 VALUES(?,?,?)",table2)

    return conn

