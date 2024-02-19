from timeit import default_timer as timer
import random

set1 = set('geEks')  # creating a set using string

for val in set1:
    print(val)  # iterating using for loop


def test_func(test_set1):  # function under evaluation
    for val1 in test_set1:
        _ = val1


if __name__ == '__main__':

    random.seed(21)

    for _ in range(5):
        test_set2 = set()

        for el in range(int(1e6)):  # generating a set of random numbers
            # el = random.random()
            test_set2.add(el)

        start = timer()
        test_func(test_set2)
        end = timer()

        print(str(end - start))
