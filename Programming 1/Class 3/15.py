import math

def calculate_grade(math, chem, phys, bio, comp):
    if result >= 90:
       return 'You received Grade A'
    elif result >= 80:
        return 'You received Grade B'
    elif result >= 70:
        return 'You received Grade C'
    elif result >= 60:
        return 'You received Grade D'
    elif result >= 40:
        return 'You received Grade E'
    else:
        return 'You received Grade F'


math = int(input('Input your percentage at Mathematics discipline: '))
chem = int(input('Input your percentage at Chemistry discipline: '))
phys = int(input('Input your percentage at Physics discipline: '))
bio = int(input('Input your percentage at Biology discipline: '))
comp = int(input('Input your percentage at Computer discipline: '))

result = (phys + chem + math + bio + comp) / 5

if calculate_grade(math, chem, phys, bio, comp):
    result = calculate_grade(math, chem, phys, bio, comp)
    print(result)
