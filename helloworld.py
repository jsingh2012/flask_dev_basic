from flask import Flask, render_template
from flask import request
from flask import redirect
from flask_bootstrap import Bootstrap
import datetime
from flask import abort
import os

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())

@app.route('/user/')
def user():
    return render_template('user.html')

@app.route('/userid/<id>')
def get_user(id):
    return render_template('user.html', user=id)

def load_user(id):
    return None

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
