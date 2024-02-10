# Using translate()

str1 = 'geeks_for_geeks'

str2 = str1.translate({ord(item): None for item in '_'})

print(str2)
