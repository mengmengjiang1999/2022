from flask import Flask, escape, url_for, request, render_template, jsonify
app = Flask(__name__)

@app.route('/hello')
def hello_world():
   return 'Hello World'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/')
def index():
    return 'Index'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))


@app.route('/algorithm/dijkstra')
def dijkstra():
    N = request.form['N']

    data = {
        'N': N,
        'form': N+N,
    }
    return jsonify(data)

with app.test_request_context():
    print(url_for('index'))
    print(url_for('hello', next='/'))
    print(url_for('profile', username='John Doe'))


if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug = True)