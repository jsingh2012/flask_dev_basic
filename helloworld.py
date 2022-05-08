from flask import Flask, render_template
from flask import request
from flask import redirect
from flask import abort

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return redirect('http://youtube.com')

@app.route('/userid/<id>')
def get_user(id):
    return render_template('user.html', name=id)

def load_user(id):
    return None
