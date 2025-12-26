# pandas is used to read CSV files (like Excel tables)
import pandas as pd

# matplotlib is used to draw graphs
import matplotlib.pyplot as plt

# os helps with file and folder paths
import os

# import the Kalman Filter class we wrote
from kalman_filter import KalmanFilter


# get the folder where this main.py file is located (src folder)
base_dir = os.path.dirname(__file__)

# go one step back to the main project folder
project_dir = os.path.dirname(base_dir)

# build the full path to the CSV file inside data folder
csv_path = os.path.join(project_dir, "data", "temperature.csv")

# read the CSV file into a table
data = pd.read_csv(csv_path)

# get the time column from the table
time = data["time"]

# get the noisy temperature values (sensor readings)
measured_temperature = data["temperature"]

# create Kalman Filter object
kf = KalmanFilter()

# empty list to store filtered temperature values
filtered_temperature = []

# go through each noisy temperature value one by one
for temp in measured_temperature:
    # send noisy value into Kalman Filter
    filtered_value = kf.update(temp)
    
    # store the filtered value
    filtered_temperature.append(filtered_value)

# start a new plot
plt.figure()

# plot noisy temperature values
plt.plot(time, measured_temperature, label="Noisy temperature")

# plot filtered temperature values
plt.plot(time, filtered_temperature, label="Filtered Temperature")

# label x-axis
plt.xlabel("Time")

# label y-axis
plt.ylabel("Temperature")

# add title to the graph
plt.title("SSM (Kalman Filter) Temperature Estimation")

# show legend (line names)
plt.legend()

# show the final graph
plt.show()
