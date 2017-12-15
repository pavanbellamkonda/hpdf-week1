from flask import Flask, render_template

app = Flask(__name__)

@app.route('/image')
def image():
    return render_template('qindex.html', image = ("image.jpg"))

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug='True')