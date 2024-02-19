import os
from pathlib import Path

size1 = os.path.getsize('Data.csv')  # With os module

size2 = Path('Data.csv').stat().st_size  # Using pathlib

print('\n', size1, '\n', size2)
