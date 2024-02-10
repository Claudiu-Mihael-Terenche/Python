# Using eval()

code = '6 + 5'

res1 = eval(code)

print(res1) # Output: 11

# Approach 2: Python program to illustrate use of exec to execute a given code as string using exec() function

def exec_code():
    LOC = """
def factorial(num):
	fact = 1
	for item in range(1, num + 1):
		fact = fact * item
	return fact
print(factorial(5))
"""
    exec(LOC)


exec_code()
