import random
import csv
import os

# build correct path
base_dir = os.path.dirname(__file__)        # src/
project_dir = os.path.dirname(base_dir)     # project root
data_dir = os.path.join(project_dir, "data")

# make sure data folder exists
os.makedirs(data_dir, exist_ok=True)

output_path = os.path.join(data_dir, "temperature.csv")

true_temperature = 20
num_points = 100

with open(output_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["time", "temperature"])

    for t in range(1, num_points + 1):
        noise = random.uniform(-1, 1)
        measured_temp = true_temperature + noise
        writer.writerow([t, round(measured_temp, 2)])

print("temperature.csv created inside data folder")
