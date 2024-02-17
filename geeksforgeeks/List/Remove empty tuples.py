# Python program to remove empty tuples from a list of tuples using lambda function
tup = [(), ('ram', '15', '8'), (), ('layman', 'sita'), ('krishna', 'akbar', '45'), ('', ''), ()]

tup = list(filter(lambda item: len(item) > 0, tup))

print(tup)
