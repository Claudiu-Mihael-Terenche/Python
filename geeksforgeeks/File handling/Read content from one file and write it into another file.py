with open('gfg input file.txt', 'r') as input0:
    with open('gfg output file 1.txt', 'w') as output:
        for line in input0:
            output.write(line)

output_file = open('gfg output file 2.txt', 'w')

with open('gfg input file.txt', 'r') as scan:
    output_file.write(scan.read())

output_file.close()

'''
# Using loops
# Taking "gfg input file.txt" as input file
# in reading mode

with open('gfg input file.txt', 'r') as input:
    # creating "gfg output file.txt" as output
    # file in write mode
    with open('gfg output file 1.txt', 'w') as output:
        for line in input: # writing each line from input file to output file using loop
            output.write(line)

# using file methods creating an output file in writing mode
output_file = open('gfg output file 2.txt', 'w')

# opening input file and scanning each line from input file and writing in output file
with open('gfg input file.txt', 'r') as scan: output_file.write(scan.read())

output_file.close() # closing the output file
'''
