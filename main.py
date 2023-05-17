from flask import Flask, render_template,request
from logging import debug
import joblib

app = Flask(__name__)
# load model

model = joblib.load('hiring_model.pkl')


@app.route('/')
def welcome():
   return render_template('basic.html')

@app.route('/predict', methods = ['POST'])
def predict():

    exp  = request.form.get('experience')
    score = request.form.get('test_score')
    interview_score = request.form.get('interview_score')

    print(type(exp))

    prediction =model.predict([[int(exp), int(score), int(interview_score)]])

    output = round(prediction[0],2)



    return render_template('basic.html', prediction_text = f'Employee salary will be : ${output}')

app.run(debug=True)
