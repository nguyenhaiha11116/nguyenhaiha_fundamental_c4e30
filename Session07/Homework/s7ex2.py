from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/user/<username>')
def index(username):
    person_data={
        'ha':
    {
        'name':'Nguyễn Hải Hà',
        'gender':'male',
        'age':'25',
        'hobbies' : 'nhân phẩm'
    },
        'nguyen':
    {
        'name':'Nguyễn Tùng Nguyên',
        'gender':'female',
        'age':'25',
        'hobbies' : 'nhảy dây'
    }}
    if username in person_data:
        return render_template('user.html',data = person_data[username])
    else:
        return 'User not found'

if __name__ == '__main__':
  app.run(host = '127.0.0.1', port=8000, debug=True)