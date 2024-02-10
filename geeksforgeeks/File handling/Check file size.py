import os
from pathlib import Path

# With os module

size1 = os.path.getsize('Data.csv')

# Using pathlib

size2 = Path('Data.csv').stat().st_size

print('\n', size1, '\n', size2)
