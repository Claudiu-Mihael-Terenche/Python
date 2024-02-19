import os

path = input('Enter folder path: ')

os.chdir(path)


def read_text_file(file_path1):
    with open(file_path1, 'r') as f:
        print(f.read())


for file in os.listdir():
    if file.endswith('.txt'):
        file_path2 = f'{path}\{file}'  # ???
        read_text_file(file_path2)

'''
# import module
import os

# folder path
path = input('Enter folder path: ') # no " " for path

os.chdir(path) # change the directory

def read_text_file(file_path): # read text file
with open(file_path, 'r') as f:
print(f.read())


for file in os.listdir(): # iterate through all file
if file.endswith('.txt'): # check whether file is in text format or not
file_path = f'{path}\{file}'

read_text_file(file_path) # call read text file function
'''
