import mysql.connector

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    password = 'hhdhhdhhd',
    autocommit = True
    )

def getAirportAndTown(ICAO):
    sql="select name, municipality from airport"
    sql+=" where ident = '" + ICAO + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"ICAO:{ICAO}\nAirport name:{row[0]}\nLocation:{row[1]}")
    return

ICAO = input("Please enter the ICAO code: ")
getAirportAndTown(ICAO)