#intertools: product, permutations, combinations, accumulate, groupby, and inifite iterators
from itertools import combinations_with_replacement, product
from itertools import permutations
from itertools import combinations
from itertools import accumulate
from itertools import groupby
import operator

a = [4, 5]
b = [6]
prod = product(a, b)
print(list(prod)) # This output the combinations of 'a' and 'b'
prod = product(a, b, repeat=2) #This will duplicate the product twice
print(list(prod))

c = [1,2,3]
perm = permutations(c)
print(list(perm))

d = [7,8,9,10]
comb = combinations(d, 2) #The second argument is mandatory which needs to know the length i.e. (#,#) is 2, (#, #,#) is 3
print(list(comb))

e = [17,18,11,12]
comb_wr = combinations_with_replacement(e, 2) # combination with itself 
print(list(comb_wr))

#Accumulate
f = [13,19,32,20,21]
acc = accumulate(f, func=operator.mul) # the second argument uses the 'operator' module to multiply each element in f.
acc2 = accumulate(f, func=max)
print(f)
print(list(acc))
print(list(acc2))

#Grouby
def smaller_than_25(x):
    return x < 25

g = [22, 23, 25, 28]
group_obj = groupby(g, key=smaller_than_25) #grouby uses the smaller_than_25 method in the 2nd argument to check the list elemts if it meets the condition x < 25
for key, value in group_obj: #This for loop
    print(key, list(value))