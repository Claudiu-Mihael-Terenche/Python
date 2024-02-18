country_code = {'India': '0091', 'Australia': '0025', 'Nepal': '00977'}

try:
    print(country_code['India'])
    print(country_code['USA'])
except KeyError:
    print('Not found')

print(country_code.get('India', 'Not found'))  # search dictionary for country code of India
print(country_code.get('Japan', 'Not found'))  # search dictionary for country code of Japan

if 'USA' in country_code:
    print(country_code['USA'])
else:
    print('Not found')

'''
# Using the try-except block
country_code = {'India': '0091', 'Australia': '0025', 'Nepal': '00977'}

try:
print(country_code['India'])
print(country_code['USA'])
except KeyError:
print('Not found')

# Using get()
# country_code = {'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977'}

print(country_code.get('India', 'Not found')) # search dictionary for country code of India
print(country_code.get('Japan', 'Not found')) # search dictionary for country code of Japan

# Using key()
# country_code = {'India': '0091', 'Australia': '0025', 'Nepal': '00977'}

if 'USA' in country_code:
print(country_code['USA'])
else:
print('Not found')
'''
