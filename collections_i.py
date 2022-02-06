#collections: counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque


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


Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt.x, pt.y)

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['e'] = 5 #Prints out top to bottom
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)

d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['b']) #calling a value that doesn't exist it will return 0 (compared to a regular dictionary, as it would return KeyError)

de = deque()
de.append(1)
de.append(2)
de.appendleft(3)
de.append(6)
print(de)

de.pop()
de.popleft()
print(de)