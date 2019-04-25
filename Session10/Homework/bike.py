from flask import Flask, render_template, redirect, request, url_for
from db import add_bike,all_bike
app = Flask(__name__)

@app.route('/new-bike',methods = ['POST'])
def post_bike():
  model = request.form.get('model')
  fee = request.form.get('fee')
  image = request.form.get('image_url')
  year = request.form.get('year')
  add_bike(model,fee,image,year)
  return render_template('add_bike.html',data = all_bike())
  
@app.route('/new-bike')
def get_bike():
  return render_template('add_bike.html',data = all_bike())

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)