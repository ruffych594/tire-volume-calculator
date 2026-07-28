# The program made use of functions and went further to nest function
# The program imported the math module and datetime
# The program also made use of if statement
# The program also use error handling to correct errors
import math
from datetime import datetime

def volume_txt(width, ratio, diameter, volume, phone = ''):
	with open('volume.txt', 'at') as file_volume:
		print(f'{datetime.now():%Y-%m-%d}, {width}, {ratio}, {diameter}, {volume: .2f}, {phone}', file = file_volume)

def tire_volume():
	width = int(input('Enter the width of the tire in mm (ex 205): '))
	ratio = int(input('Enter the aspect ratio of the tire (ex 60): '))
	diameter = int(input('Enter the diameter of the whell in inches (ex 15): '))

	numerator = math.pi * math.pow(width, 2) * ratio * ( width * ratio + 2540 * diameter)
	denominator = 10_000_000_000

	volume = numerator / denominator

	phone = ''


	# Calling the volume_txt function with 4 arguements
	volume_txt(width, ratio, diameter, volume, phone)
	

	print(f'The approximate volume is {volume: .2f} litres')
	print()

	try:
		# Checking whether the customer wants to buy or not
		cust_answer = input('Would you like to buy tires with the dimensions that you have entered: "Yes" or "No" ')
		if 'yes' == cust_answer.lower().strip():
			phone = input('Please provide us with your phone number: ')
			if phone.strip() == '':
				raise ValueError ('Phone number cannot be empty if you want us to call you')
			
		else:
			
			print(f'Thank you, hope next time we will be able to meet your requirements')

	except Exception as e:
		
		print(f'Error: {e}')

	# Calling the volume_txt function with 4 arguements
	volume_txt(width, ratio, diameter, volume, phone)
	

# This is the main guard to the program
if __name__ == '__main__':
	tire_volume()
