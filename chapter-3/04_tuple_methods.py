b = (1, "rohan", "mohan", 1,1,1,1,1,2,98) # multiple element tuple
print(b)

no = b.count(1)
print(no)

# Example
t = (1, 2, 3, 1, 1)

print(t.index(1))  # Output: 0

print(t.index(1, 1))  # Output: 3 (starts searching from index 1)

i = t.index(3)

print(i)
print(len(t))