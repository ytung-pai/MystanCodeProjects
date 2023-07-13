"""
File: weather_master.py
Name: Yutung
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -100

def main():
	"""
	This is a program that computes the highest, lowest, average temperature, and cold days
	among user's data.
	"""
	print('stanCode "Weather Master 4.0"' + '!')
	temperature_list = []
	n = int(input('Next Temperature: (or -100 to quit)? '))
	if n == -100:
		print('No temperatures were entered.')
	else:
		while True:
			if n != EXIT:
				temperature_list.append(n)
				# adding the input int into the list
				n = int(input('Next Temperature: (or -100 to quit)? '))
				# reassigning n value
			else:
				break

		print('Highest temperature = ' + str(max(temperature_list)))
		print('Lowest temperature = ' + str(min(temperature_list)))
		mean_temperature = sum(temperature_list) / len(temperature_list)
		print('Average = ' + str(round(mean_temperature, 1)))
		cold_days = len([x for x in temperature_list if x < 16])
		print(str(cold_days) + ' cold day(s)')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
