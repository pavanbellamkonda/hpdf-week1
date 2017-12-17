from flask import Flask, render_template, url_for, redirect, request, make_response
import requests
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"
    
@app.route('/authors', methods=['POST', 'GET'])
def authors():
    u = 'https://jsonplaceholder.typicode.com/users'
    p = 'https://jsonplaceholder.typicode.com/posts'

    ur = requests.get(u)
    pr = requests.get(p)

    ud = ur.text
    pd = pr.text

    users = json.loads(ud)
    posts = json.loads(pd)

    id = []
    names = []
    count = []
    for i in range(len(users)):
        id.append(users[i]["id"])
        names.append(users[i]["name"])
        count.append(0)

    for i in range(len(users)):
        for j in range(len(posts)):
            if id[i] == posts[j]["userId"]:
                count[i] = count[i] + 1


    return render_template('authors.html', count = count, names = names, id = id)
    
@app.route('/setcookie')
def setcookie():
    return render_template('index.html')

@app.route('/index', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        user = request.form['nm']
        age = request.form['age']
        resp = make_response(redirect(url_for('getcookie')))
        resp.set_cookie('Pavan', user)
        resp.set_cookie('19', age)
        return resp

@app.route('/getcookies')
def getcookie():
    name = request.cookies.get('Pavan')
    age = request.cookies.get('19')
    return '<h2>Name: '+name+' Age: '+age+'</h2>'

@app.route('/robots.txt')
def deny():
    return redirect('http://httpbin.org/deny')
    
 
@app.route('/image')
def image():
    return render_template('qindex.html', image = ("image.jpg"))

@app.route('/input')
def input():
    return render_template('input.html')

@app.route('/log', methods=['POST'])
def log():
    user = request.form['name']
    str1.append(user)
    return redirect(url_for('success'))

@app.route('/success')
def success():
    print(str1)
    return render_template('success.html', names = str1)


if __name__ == '__main__':
    app.run(host='localhost',port=8080,debug=True)
