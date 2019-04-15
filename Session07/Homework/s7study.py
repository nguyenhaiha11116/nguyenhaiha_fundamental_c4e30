from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/about-me')
def index():
    person_data=[{
      'name':'Nguyễn Hải Hà',
      'work':'IT',
      'school':'NUCE',
      'hobbies' : 'nhân phẩm'
    }]
    return render_template('about_me.html',data = person_data)

@app.route("/school")
def school():
    return redirect('http://techkids.vn')

if __name__ == '__main__':
  app.run(host = '127.0.0.1', port=8000, debug=True)