#intertools: product, permutations, combinations, accumulate, groupby, and inifite iterators
from itertools import product

a = [1, 2]
b = [3, 4]
prod = product(a, b)
print(list(prod)) # This output the combinations of 'a' and 'b'
prod = product(a, b, repeat=2) #This will repeat the product 2x
print(list(prod))