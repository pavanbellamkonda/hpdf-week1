from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/setcookie', methods=['POST','GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']
        age = request.form['age']
        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie('Pavan', user)
        resp.set_cookie('19', age)
        return resp

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('Pavan')
    age = request.cookies.get('19')
    return '<h2>Name: '+name+' Age: '+age+'</h2>'

if __name__ == '__main__':
    app.run(host='localhost',port=8080,debug=True)