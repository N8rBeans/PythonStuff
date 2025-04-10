#####################################################################################
# IMPORTS
#####################################################################################

import csv
import matplotlib.pyplot as plt

#####################################################################################
# DATA
#####################################################################################

# arbitrary data
# represents time in seconds and distance in meters
data = [
    (1, 20.5),
    (2, 22.3),
    (3, 21.0),
    (4, 19.8),
    (5, 23.1)
]

#####################################################################################
# GENERATE CSV
#####################################################################################

# if file does not exist yet, it automatically creates one
with open('test_data.csv', 'w', newline='') as file:
	# begin writing
	writer = csv.writer(file)

	# write header
	writer.writerow(["Day", "Temperature"])

	# write rows (will follow same (time, distance) format from tuples in data)
	writer.writerows(data)

#####################################################################################
# READ CSV
#####################################################################################

# empty data lists
times = []
distances = []

# open file
with open('test_data.csv', 'r') as file:
	# begin reading
	reader = csv.reader(file)

	# skip header line
	next(reader)

	# loop through all rows and fill in data
	for row in reader:
		times.append(row[0])
		distances.append(float(row[1]))

#####################################################################################
# PLOT CSV
#####################################################################################

plt.plot(times, distances, linestyle = '-', color = 'orange')
plt.title('Sensor Data')
plt.xlabel('Time (s)')
plt.ylabel('Distance (m)')
plt.grid(True)
plt.show()