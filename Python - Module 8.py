
#Question 1
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

########################################
#Question 2
import mysql.connector

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = '3306',
    database = 'flight_game',
    user = 'root',
    password = 'hhdhhdhhd',
    autocommit = True
    )

def getAirportType(areaCode):
    sql = "select name, type from airport"
    sql+= " where iso_country = '" + areaCode + "'"
    sql+= " order by type" 
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"{row[0]}\t\t\t\t{row[1]}")
    return

areaCode = input("Please enter the area code: ")
getAirportType(areaCode)

########################################
# Question 3
from geopy import distance
import mysql.connector

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = '3306',
    database = 'flight_game',
    user = 'root',
    password = 'hhdhhdhhd',
    autocommit = True
    )

def getDistance(ICAO1, ICAO2):
    sql1 = f"select latitude_deg, longitude_deg from airport where ident = '{ICAO1}'"
    cursor1 = connection.cursor()
    cursor1.execute(sql1)
    result1 = cursor1.fetchall()
    sql2 = f"select latitude_deg, longitude_deg from airport where ident = '{ICAO2}'"
    cursor2 = connection.cursor()
    cursor2.execute(sql2)
    result2 = cursor2.fetchall()

    return distance.distance(result1,result2)


areaCode1 = input("Please enter the first area code: ")
areaCode2 = input("Please enter the second area code: ")
print(getDistance(areaCode1,areaCode2))

    

    


