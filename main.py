from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained AI "brain" we just created [cite: 562]
model = joblib.load("predictive_maintenance_model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    # Receive the sensor data from the request [cite: 565]
    data = request.get_json()
    
    # Extract readings: temperature, vibration, and current [cite: 566]
    features = np.array([[data["temperature"], data["vibration"], data["current"]]])
    
    # Ask the AI to predict [cite: 567]
    prediction = model.predict(features)
    
    # Determine the status message [cite: 568]
    status = "Machine failure predicted!" if prediction[0] == 1 else "Machine is running normally."
    
    return jsonify({"Prediction": status})

if __name__ == '__main__':
    print("AI Predictive Maintenance API is starting...")
    app.run(debug=True)