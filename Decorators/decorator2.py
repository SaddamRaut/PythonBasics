from time import sleep

"""
Decorator defination
"""
def sleepDecorator(function):
	"""
	Modified how fast function to be executes
	"""

	def addFunctionality(num):
		sleep(2)
		return function(num)		

	return addFunctionality




@sleepDecorator
def printNumber(num):
	"""
	Simple Function which returns its parameter
	"""
	return num

if __name__ == "__main__":
	#call
	print(printNumber(123))

	#call with for loop
	for  num in range(1, 10):
		print(printNumber(num))
