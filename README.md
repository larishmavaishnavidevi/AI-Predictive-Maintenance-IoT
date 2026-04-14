# AI-Powered Predictive Maintenance for IoT Devices

## Project Explanation
[cite_start]This project is an AI-powered predictive maintenance system that predicts machine failures in advance using IoT sensor data like temperature, vibration, and current[cite: 5, 243]. [cite_start]It solves the problem of reactive maintenance by reducing downtime and improving efficiency[cite: 19, 28, 30].

## Tech Stack
* [cite_start]**Python:** Main programming language [cite: 59, 298]
* [cite_start]**Libraries:** Pandas, NumPy, Scikit-learn, and Joblib [cite: 60, 61, 62, 546]
* [cite_start]**API:** Flask for real-time predictions [cite: 300, 548]

## [cite_start]Project Architecture [cite: 66, 67]
1. [cite_start]**Data Collection:** Simulates sensors for temperature, vibration, and current[cite: 305, 307].
2. [cite_start]**Preprocessing:** Data cleaning and normalization[cite: 84, 516].
3. [cite_start]**Model:** Random Forest Classifier used to predict machine failures[cite: 527, 539, 568].
4. [cite_start]**Deployment:** Flask API to handle incoming sensor data requests[cite: 552, 554].

## How to Run
1. [cite_start]Install dependencies: `pip install -r requirements.txt` [cite: 118, 120]
2. Generate dataset: `python data_generator.py`
3. Train model: `python train_model.py`
4. [cite_start]Start API: `python main.py` [cite: 156, 157]