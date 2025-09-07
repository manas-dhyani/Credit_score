
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def index():
    """Render home page with input form."""
    return render_template('index.html', features=['prospect_no', 'asset_cost', 'down_payment', 'roi', 'age', 'is_exist_cust', 'dist_from_off', 'is_expat', 'children', 'earning_members', 'yrs_in_curr_resi', 'veh_own', 'foir', 'tenure', 'vin_in_business', 'itv', 'itvg'])

@app.route('/predict', methods=['POST'])
def predict():
    """
    Collects input parameters from form, predicts credit risk, 
    and returns prediction result.
    """
    input_data = []
    for feature in ['prospect_no', 'asset_cost', 'down_payment', 'roi', 'age', 'is_exist_cust', 'dist_from_off', 'is_expat', 'children', 'earning_members', 'yrs_in_curr_resi', 'veh_own', 'foir', 'tenure', 'vin_in_business', 'itv', 'itvg']:
        val = float(request.form.get(feature))
        input_data.append(val)
    arr = np.array([input_data])
    pred = model.predict(arr)[0]
    result = 'High Risk' if pred == 1 else 'Low Risk'
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
