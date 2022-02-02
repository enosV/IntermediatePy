#Strings: ordered, immutable, text representation

my_string = "Hello World"
print(my_string)

my_string2 = "Hello World 2"
print(type(my_string2))

#continue to the next line but prints out to the same line, backslash.
my_string2 = "Hello \
World"
print(my_string2)

#Using indexes to select characters
my_string3 = "Hello World"
char1 = my_string3[0]
char2 = my_string3[-1]
#If you try and change a char like, char3[0] = 'h', then you'll get a Type Error since strings are immutable
print(char1)
print(char2)

#Slicing so it starts at index 1 and goes through index 4, but stops at index 5
my_string4 = "Hello World"
substring = my_string4[1:5]
print(substring)

#Skip through characters by using double colon, :: and specify the frequency to skip, and can even reverse a string using a -1
my_string5 = "Hello World"
substring2 = my_string4[::-1]
print(substring2)

#Concat
greeting = "Hello"
name = "Alex"
sentence = greeting + " " + name
print(sentence)

#This is print out the string vertically by iterating through the string 
greeting2 = "Hola"
for x in greeting2:
    print(x)

#You can just code in the string too
for y in "hola":
    print(y)

#Check to see if a char or a series of chars exists within a string, true or false. 
greeting3 = "Hello"
if 'e' in greeting3:
    print('yes')
else:
    print('no')

#Removing whitespace
my_string6 = '     Hello World'
my_string6 = my_string6.strip() #This is what will strip the string of the whitespace but it needs to be reassigned doing only my_string6.strip() won't work as strings are not mutable. 
print(my_string6)

#Convert to lowercase
my_string7 = "Hello wOrLd"
print(my_string7.lower())

#Check to see if the strings starts or ends with a certain letter or word
my_string8 = "Hello World"
print(my_string8.startswith('World')) #false
print(my_string8.startswith('H')) #True
print(my_string8.startswith('Hello')) #True
print(my_string8.endswith('World')) #True

#Finding the char index in the string
my_string9 = "Hello World"
print(my_string9.find('lo')) #index 3
print(my_string9.find('g')) #index is not found so it prints -1

#Counting the characters in the string
my_string10 = "Hello World"
print(my_string10.count('o')) #This will count the number of times the o character appears in my_string10

#Create a new string by replacing a word in the original string 
my_string11 = "Hello World"
print(my_string11.replace('World', 'Universe')) #This will CREATE a new string from the old (if the word is not found then nothing happens)

#Convert a string to a lise using split
my_string12 = 'How are you doing'
my_list = my_string12.split() #By default split uses space as a delimiter but you can speficy a "," delimiter if the string is seperated as such (see example below)
print(my_list)

#Converting back to a string
my_string13 = 'how,are,you,doing'
my_list2 = my_string13.split(',')
print(my_list2)
new_string = ' '.join(my_list2)
print(new_string)

#Joining a list to a string
my_list3 = ['a'] * 6
print(my_list3)

my_string14 = ''
for i in my_string14:
    my_string14 += i #this line is slow so its bad
print(my_string14)

my_string15 = ''.join(my_list3) #this is much faster so its good
print(my_string15)

#%, .format(), f-Strings
var = 3.1234567 
my_string16 = "the variable is %.2f" %var #This is the old style where you speficy which variable to % and then tell it how many decimal places we can to print
print(my_string16)

var2 = 3.1234567
var3 = 6
my_string17 = "the variable is {:.2f} and {}".format(var2,var3) #This is the old style wher you can also speficy multiple variables
print(my_string17)

var4 = 3.1234567
var5 = 6
my_string18 = f"the variable is {var4*2} and {var5}" #This the new style after 3.6 and can even evaluate the variables at run time for example, var*2
print(my_string18)
