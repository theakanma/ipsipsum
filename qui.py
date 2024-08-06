tuple = {}
counts = [1, 2, 3]
cell = {'num': 42}

for i in range(len(counts)):
    tuple[counts[i]] = cell['num']

print(tuple)  # Output: {1: 42, 2: 42, 3: 42}
