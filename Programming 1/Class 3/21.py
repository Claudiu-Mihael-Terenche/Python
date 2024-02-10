import math

def calculate_grade(math, chem, phys, bio, comp):
    if result >= 60:
       return 'You are in the First Division'
    elif result >= 50:
        return 'You are in the Second Division'
    elif result >= 40:
        return 'You are in the Third Division'
    else:
        return 'You Failed'


math = int(input('Input your percentage at Mathematics discipline: '))
chem = int(input('Input your percentage at Chemistry discipline: '))
phys = int(input('Input your percentage at Physics discipline: '))
bio = int(input('Input your percentage at Biology discipline: '))
comp = int(input('Input your percentage at Computer discipline: '))

result = (phys + chem + math + bio + comp) / 5

if calculate_grade(math, chem, phys, bio, comp):
    result = calculate_grade(math, chem, phys, bio, comp)
    print(result)
