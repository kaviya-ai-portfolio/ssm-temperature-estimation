# import pandas to read CSV files easily
import pandas as pd

# import matplotlib to draw plots
import matplotlib.pyplot as plt

# import os to handle file paths safely
import os


# get path of this file (src folder)
base_dir = os.path.dirname(__file__)

# go one level up to project folder
project_dir = os.path.dirname(base_dir)

# build full path to CSV file
csv_path = os.path.join(project_dir, "data", "temperature.csv")


# read CSV file into a table (DataFrame)
data = pd.read_csv(csv_path)


# print first 5 rows to check data
print("First 5 rows of dataset:")
print(data.head())


# extract time values
time = data["time"]

# extract temperature values
temperature = data["temperature"]


# create a plot
plt.figure()

# plot temperature vs time
plt.plot(time, temperature)

# label x-axis
plt.xlabel("Time")

# label y-axis
plt.ylabel("Temperature")

# add title to plot
plt.title("Noisy Temperature Data")

# show the plot on screen
plt.show()
