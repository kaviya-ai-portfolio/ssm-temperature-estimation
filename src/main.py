import pandas as pd
import matplotlib.pyplot as plt
import os

from kalman_filter import KalmanFilter

base_dir = os.path.dirname(__file__)

project_dir = os.path.dirname(base_dir)


csv_path = os.path.join(project_dir,"data","temperature.csv")

data = pd.read_csv(csv_path)

time=data["time"]
measured_temperature=data["temperature"]

kf=KalmanFilter()

filtered_temperature=[]

for temp in measured_temperature:
    filtered_value = kf.update(temp)
    filtered_temperature.append(filtered_value)
    
plt.figure()
plt.plot(time, measured_temperature, label="Noisy temperature")
plt.plot(time, filtered_temperature, label="Filtered Temperature")
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.title("SSM (Kalman Filter) Temperature Estimation")
plt.legend()
plt.show()
    


