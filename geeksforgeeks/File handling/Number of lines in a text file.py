# Using readlines()

with open(r'gfg input file.txt', 'r') as fp:
	lines = len(fp.readlines())
	print('Total number of lines:', lines)
