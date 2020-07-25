import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from flask import Flask, render_template, request, redirect, url_for
import pickle

# start flask
app = Flask(__name__)


# render HomePage
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


# Predict using the model
@app.route('/predicted', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Load all values from the form to our model
            Pregnancies = float(request.form['preg'])
            Glucose = float(request.form['gluc'])
            BloodPressure = float(request.form['bp'])
            SkinThickness = float(request.form['st'])
            Insulin = float(request.form['ins'])
            BMI = float(request.form['bmi'])
            DiabetesPedigreeFunction = float(request.form['dpf'])
            Age = float(request.form['age'])

            # pickle file loaded to our model
            file = 'logReg.pkl'
            model = pickle.load(open(file, 'rb'))  # model loaded

            # Standardizing file loaded
            file1 = "scalemod.pkl"
            scaled = pickle.load(open(file1, 'rb'))  # scaling loaded

            # Inputs standardized
            # model_values = np.array([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,BMI, DiabetesPedigreeFunction, Age])
            model_values = [
                [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]
            model_values = pd.DataFrame(model_values)
            scaled_values = scaled.transform(model_values)

            # Prediction
            output = model.predict(scaled_values)

            if output[0] == 0:
                output_final = "NO"
            elif output[0] == 1:
                output_final = "YES"
            else:
                output_final = "Something Went Wrong"

            # Throw output to results.html

            return render_template('results.html', prediction=output_final)
        except Exception as e:
            return render_template('results.html', prediction=e)


# To keep the app running
if __name__ == '__main__':
    # app.run(host='localhost', port=80)
    app.run(debug=True)

