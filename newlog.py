from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

str1 = []

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
    app.run(host='localhost', port=8080, debug='True')