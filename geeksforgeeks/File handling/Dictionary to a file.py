# Without using loads(),dumps()

details = {'Name': 'Bob', 'Age' :28}

with open('file.txt','w') as data: data.write(str(details))

# Using loop

details = {'Name': 'Alice', 'Age': 21, 'Degree': 'Bachelor Cse', 'University': 'Northeastern Univ'}

with open('myfile.txt', 'w') as f:
	for key, value in details.items():
		f.write('%s:%s\n' % (key, value))
