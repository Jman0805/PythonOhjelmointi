from flask import Flask

app = Flask(__name__)
@app.route('/alkuluku/<num>')
def alkuluku(num):
    alkuluku = True

    num = int(num)

    for i in range(2, num):
        if num % i == 0:
            alkuluku = False
    vastaus = {
        "Number" : num,
        "isPrime" : alkuluku
    }
    return str(vastaus)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)


