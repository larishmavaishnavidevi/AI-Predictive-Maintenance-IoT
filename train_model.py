import pandas as pd
from sklearn.ensemble import RandomForestClassifier # Model type [cite: 50, 64]
from sklearn.model_selection import train_test_split
import joblib

# Load the virtual dataset [cite: 83, 126]
df = pd.read_csv('iot_sensor_data.csv')
X = df[['temperature', 'vibration', 'current']]
y = df['failure']

# Split into training and testing sets [cite: 537]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Build the model [cite: 86, 129]
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model as a .pkl file [cite: 522, 547]
joblib.dump(model, 'predictive_maintenance_model.pkl')
print("AI Model 'predictive_maintenance_model.pkl' has been trained and saved!")