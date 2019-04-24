import itertools

x = ('Sm', 'Tb', 'Hf', 'Er', 'Y', 'Al', 'Cu', 'Ni', 'Ti')

alloys = itertools.combinations(x, 4)

for x in alloys:
    a = "".join(x)
    print(a)

# 1  - 9
# 2  - 36
# 3  - 84
# 4  - 126
# 5  - 126
# 6  - 84
# 7  - 36
# 8  - 9
# 9  - 1
