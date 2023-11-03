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