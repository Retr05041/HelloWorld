from flask import Flask, request

app = Flask(__name__)

# @ signifies a decorator -- way to wrap a function and modifying its behavoir
@app.route('/')
def index():
    return 'Homepage'

@app.route('/tuna')
def tuna():
    return '<h2>Tuna is good</h2>'

@app.route("/method")
def method():
    return 'You are using GET'

@app.route("/method2", methods=['GET', 'POST'])
def method2():
    if request.method == 'POST':
        return 'You are using POST'
    else:
        return 'You are using GET'

@app.route('/profile/<username>')
def profile(username):
    return '<h2>Hey there %s</h2>' % username

@app.route('/post/<int:post_id>')
def post(post_id):
    return '<h2>post ID is  %s</h2>' % post_id



if __name__ == '__main__':
    app.run()
