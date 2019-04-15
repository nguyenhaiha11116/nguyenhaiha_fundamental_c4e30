from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/bmi/<int:weight>/<int:height>')
def calculate(weight,height):
    person_data={
      'weight':weight,
      'height':height,
      'bmi':weight/((height*height)/10000)
    }
    return render_template('bmi.html',data = person_data)

    # bmi = weight/((height*height)/10000)
    # if bmi < 16:
    #     return 'BMI<16 : Severely underweight'
    # elif bmi <18.5:
    #     return '16<=BMI<18.5 : Underweight'
    # elif bmi < 25:
    #     return '18.5<=BMI<25 : Normal'
    # elif bmi <30:
    #     return '25<=BMI<30 : Overweight'
    # else:
    #     return 'BMI>=30 : Obese'

if __name__ == '__main__':
  app.run(host = '127.0.0.1', port=8000, debug=True)