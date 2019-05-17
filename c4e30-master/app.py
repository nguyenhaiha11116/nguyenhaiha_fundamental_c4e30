from flask import Flask, render_template, request, redirect, url_for, session
from db import find_username, add_user, get_all, find_password
app = Flask(__name__)
# app.secret_key = 'abjhejkwiooo123123'

@app.route('/signup')
def get_signup():
    return render_template('signup.html')

@app.route('/signup', methods= ["POST"])
def post_signup():
    username = request.form.get('username')
    password = request.form.get('password')
    nick_name = request.form.get('nick_name')
    if find_username(username) == None:
        add_user(username,nick_name,password)
        return render_template('index.html')
    else:
        return redirect(url_for('get_signup'))



@app.route('/')
def get_index():
    return render_template('home.html')

@app.route('/login', methods = ["POST"])
def post_index():
    username = request.form.get('username')
    password = request.form.get('password')
    # user = {
    #     'username':username,
    #     'password':password,
    # }

    a = find_username(username)
    b = find_password(a,password)
    if b == None:
        return 'sai'
    return 'đúng'

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 