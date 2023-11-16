from flask import Flask
import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='hhdhhdhhd',
         autocommit=True
         )

app = Flask(__name__)


@app.route('/airport/<ICAO>')
def airport(ICAO):
    sql = "select name, municipality from airport where ident = '" + ICAO + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    response = {
        "ICAO": ICAO,
        "Name": result[0][0],
        "Location": result[0][1]
    }
    return response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
