# Get the user's input for their score
score = int(input('Enter your score: '))

# Determine the corresponding grade based on the score
if score < 25:
    grade = 'F'
elif 25 <= score < 45:
    grade = 'E'
elif 45 <= score < 50:
    grade = 'D'
elif 50 <= score < 60:
    grade = 'C'
elif 60 <= score < 80:
    grade = 'B'
else:
    grade = 'A'

# Print the corresponding grade
print(f'You received the grade {grade}')
