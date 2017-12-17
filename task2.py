from flask import Flask, render_template
import json
import requests

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
