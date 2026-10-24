from flask import Flask, render_template, request
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
import math

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():

    actual = request.form['actual']
    predicted = request.form['predicted']

    actual_list = [float(x.strip())
                   for x in actual.split(',')]

    predicted_list = [float(x.strip())
                      for x in predicted.split(',')]

    mae = mean_absolute_error(
        actual_list,
        predicted_list
    )

    mse = mean_squared_error(
        actual_list,
        predicted_list
    )

    rmse = math.sqrt(mse)

    r2 = r2_score(
        actual_list,
        predicted_list
    )

    return render_template(
        'index.html',
        mae=round(mae, 3),
        mse=round(mse, 3),
        rmse=round(rmse, 3),
        r2=round(r2, 3)
    )


if __name__ == '__main__':
    app.run(host="0.0.0.0",port = 5000,debug=True)