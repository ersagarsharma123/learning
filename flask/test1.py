from flask import Flask

app = Flask(__name__)

@app.route('/')
def test_hello():
    return {'data': 'success'}


@app.route('/add/<int:x>/<int:y>')
def add(x,y):
    return {'data': x+y}

if  __name__ == '__main__':
    app.run(debug=True)
