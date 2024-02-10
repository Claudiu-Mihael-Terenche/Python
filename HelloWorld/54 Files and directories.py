from pathlib import Path

path = Path()
for file in path.glob('*.py'):
    print(file)

# *.* for all files
# *.py for all Python files
# *.xls for all xls files, so and on
