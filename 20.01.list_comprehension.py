### Conditionals
L = []
for i in range(10):
        if i % 3 != 0:
                L.append(i*i)
print(L)

print( [i*i for i in range(10) if i % 3 != 0] )




L = []
"""
for i in range(10):
    for j in {2, 5, 9}:
        L.append((i,j))
"""
L = [ ((i,j)) for i in range(10) for j in {2, 5, 9}]
print(L)
M = []
"""
for i in range(10):
    for j in [2, 5, 9]:
        M.append((i,j))
"""
M = [ ((i,j)) for i in range(10) for j in [2, 5, 9]]
print(M)