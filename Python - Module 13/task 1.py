from flask import Flask

app = Flask(__name__)


@app.route('/prime_number/<number>')
def prime_number(number):
    n = int(number)
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                a = False
            else:
                a = True
    else:
        a = False

    response = {
        "Number": number,
        "isPrime": a
    }
    return response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
