import pandas as pd
import random

def generate_sensor_data(rows=2000):
    data = []
    for _ in range(rows):
        # Simulated sensor readings: temperature, vibration, current [cite: 35, 69]
        temp = round(random.uniform(30, 70), 2)
        vibration = round(random.uniform(1, 4), 2)
        current = round(random.uniform(5, 15), 2)
        failure = 0 # Machine is running normally [cite: 568]
        
        # Representing machine failure [cite: 144]
        if random.random() < 0.15: 
            temp = round(random.uniform(80, 110), 2)
            vibration = round(random.uniform(6, 10), 2)
            current = round(random.uniform(20, 35), 2)
            failure = 1 # Machine failure predicted [cite: 568]
            
        data.append([temp, vibration, current, failure])
        
    df = pd.DataFrame(data, columns=['temperature', 'vibration', 'current', 'failure'])
    df.to_csv('iot_sensor_data.csv', index=False)
    print("Simulation Complete: 'iot_sensor_data.csv' created.")

if __name__ == "__main__":
    generate_sensor_data()