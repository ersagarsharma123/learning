from flask import Flask, render_template

app1 = Flask(__name__)

@app1.route('/')
def hello_world():
    return 'hello, worlds'


@app1.route('/test')
def test_api():
    return render_template('index.html')


@app1.route('/add/<int:x>/<int:y>')
def add(a,b):
    print(a,b)
    return {'data': a+b}


if __name__ == "__main__":
    app1.run(debug=True, port=8000)