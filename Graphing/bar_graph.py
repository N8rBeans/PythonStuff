import csv
import matplotlib.pyplot as plt

days = []
temperatures_1 = []

with open('sensor_data.csv', 'r') as file:
	reader = csv.reader(file)
	next(reader) # skip line
	for row in reader:
		days.append(row[0])
		temperatures_1.append(float(row[1]))

plt.bar(days, temperatures_1, linestyle = '-', color = 'orange')
plt.title('Sensor Data')
plt.xlabel('Day')
plt.ylabel('Temperature')
plt.grid(True)
plt.show()