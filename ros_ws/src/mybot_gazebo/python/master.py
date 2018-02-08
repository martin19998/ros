#!/usr/bin/env python

# Import classes for all objects in the Simulation
import carSimpleBehaviour()
import passengerSimpleBehaviour()
import sensorSimpleBehaviour()

# Set variables
car = carSimpleBehaviour()
passenger = passengerSimpleBehaviour() 	# Perhaps this one is integrated in the car because there are 					# not parameter inputs
sensor = sensorSimpleBehaviour()

# Inputs from User
max_speed = 100		# [?]
max_angle = 1.0		# [rad]
max_delay = 2.0		# [s]
interval_speed = 1.0
interval_angle = 0.05
interval_delay = 0.01

# Loop it
for i in range(0, max_speed, interval_speed):
	for j in range(0, max_angle, interval_angle):
		for k in range(0, max_delay, inerval_delay):
			car.runbehaviour(i)
			passenger.runbehaviour(j)
			sensor.run_sensor(k)
			# open in write mode, if the file does not exist it will be automatically
			# created
			# Adds a new line with parameters and results to the datasheet
			with open('datasheet', 'a') as datas:
				datas.write(results)
				datas.writelines(lines)
			



#Reset Positions and go to the beginning of the loop again (include times perhaps to give the computer some time-> to minimize errors)
