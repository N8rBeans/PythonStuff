import csv
import matplotlib.pyplot as plt

days = []
temperatures_1 = []
temperatures_2 = []

with open('sensor_data.csv', 'r') as file:
	reader = csv.reader(file)
	next(reader) # skip line
	for row in reader:
		days.append(row[0])
		temperatures_1.append(float(row[1]))
		temperatures_2.append(float(row[1]) + 5)

plt.plot(days, temperatures_1, linestyle = '-', color = 'orange')
plt.plot(days, temperatures_2, linestyle = '-', color = 'purple')
plt.title('Sensor Data')
plt.xlabel('Day')
plt.ylabel('Temperature')
plt.grid(True)
plt.savefig('test_graph.png')
plt.show()