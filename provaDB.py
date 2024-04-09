import mysql.connector
try:
    cnx = mysql.connector.connect(user='root',
                                  password='SECRET',
                                  host='127.0.0.1',
                                  database='provadb')
    cursor = cnx.cursor()
    id = int(input("inserire in input l'identificativo della persona: "))
    name = input("inserire in input il nome della persona: ")
    query = """INSERT INTO test 
               (id, nome)
               VALUES (%s, %s)"""
    query2 = "SELECT * FROM test"
    cursor.execute(query, (id, name))
    cnx.commit()
    cursor.execute(query2)
    rows = cursor.fetchall()
    print(rows)
    cursor.close()
    cnx.close()
except mysql.connector.Error as err:
    print(err)

