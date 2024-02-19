str1 = 'aacdb'
str2 = 'gafd'

set1 = set(str1)
set2 = set(str2)

uncommon = list(set1 ^ set2)

res = ''.join(uncommon)

print(res)

'''
# Using set symmetric difference 
# Function to concatenated string with uncommon
# characters of two strings

def uncommonConcat(str1, str2):

# convert both strings into set
set1 = set(str1)
set2 = set(str2)

# Performing symmetric difference operation of set
# to pull out uncommon characters
uncommon = list(set1 ^ set2)

# join each character without space to get
# final string
print( ''.join(uncommon) )

# Driver program
if __name__ == "__main__":
str1 = 'aacdb'
str2 = 'gafd'
uncommonConcat(str1,str2)
'''
