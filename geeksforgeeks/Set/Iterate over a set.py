from timeit import default_timer as timer
import itertools
import random

set1 = set('geEks') # creating a set using string

for val in set1: print(val) # iterating using for loop

def test_func(test_set): # function under evaluation

	for val in test_set:
		_ = val

if __name__ == '__main__':

	random.seed(21)

	for _ in range(5):
		test_set = set()

		for el in range(int(1e6)): # generating a set of random numbers
			el = random.random()
			test_set.add(el)

		start = timer()
		test_func(test_set)
		end = timer()

		print(str(end - start))
