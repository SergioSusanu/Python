import sys

sys.path.insert(1,r'/Users/sergiususanu/Documents/Python-1/oop/data')

import data



locations = sys.path
for i in locations:
    print(i)

print(data.names)