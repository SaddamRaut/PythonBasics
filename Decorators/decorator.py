import time


def profileFunction(targetFunction):
	"""
	Add profiling to targetFunction
	"""
	
	def wrapper():
		t1 = time.time()
		time.sleep(2)
		targetFunction()
		t2 = time.time()
		print "Function tooks : " + str(t2 - t1) + " Seconds\n"

	return wrapper

@profileFunction
def sumOfList():
	"""
	Simple Function which prints sum of list
	"""
	numList = []
	for num in range(0, 10):
		numList.append(num)
	print "Sum of list : " + str(sum(numList))


if __name__ == "__main__":
	sumOfList()

