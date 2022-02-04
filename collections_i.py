#collections: counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter
a = "aaaaaabbbbccccc"
my_counter = Counter(a)
print(my_counter) # this will create a dict with key as a string and the count as the value
print(my_counter.items()) # This will create a list with key,value pairs
print(my_counter.keys()) # This will print the keys only
print(my_counter.values()) # This will print the values only
print(my_counter.most_common(1)) #This will print the most common char and its count
print(my_counter.most_common(2)) #Same as before but the 2 most common
print(my_counter.most_common(1)[0][0]) # This brings out the most common char then access the tuple at index 0, then it selects the first element in that tuple 0.
print(list(my_counter.elements())) #This converts the string into a list of iterable strings as many times as they count