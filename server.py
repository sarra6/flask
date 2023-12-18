from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route('/dojo')
def dojo():
    return 'Dojo'
@app.route('/flask')
def dojo():
    return 'Hello flask !'

@app.route('/say/michael')
def say_name():
    return "michael"
@app.route('/JOHN')
def name():
    return 'HELLO JOHN'

@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num, word):
    output = ''

    for i in range(0,num):
        output += f"<p>{word}</p>"

    return output

if __name__=="__main__":
    app.run(debug=True)