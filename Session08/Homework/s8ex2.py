from flask import Flask, render_template, redirect, request, url_for
app = Flask(__name__)

users_info = [
    {
        'username' : 'haiha',
        'password' : 'deptrai'
    },
    {
        'username' : 'gatan',
        'password' : 'thuocbac'
    }
]
a = str('')
@app.route('/',methods=["POST"])
def get_user():
    user_name = request.form.get('user_name')
    pass_word = request.form.get('pass_word')
    userinfo = {
        'username' : user_name,
        'password' : pass_word
    }
    if userinfo in users_info:
        a = str('Login successful!')
    else:
        a = str('Login failed!')
    return render_template('login.html',data = a)

@app.route('/')
def index():
    return render_template('login.html',data = a)

if __name__ == '__main__':
  app.run(host = '127.0.0.1', port=8000, debug=True)