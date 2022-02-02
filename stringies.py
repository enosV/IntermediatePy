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
my_string6 = '     hello world'
my_string6 = my_string6.strip() #This is what will strip the string of the whitespace but it needs to be reassigned doing only my_string6.strip() won't work as strings are not mutable. 
print(my_string6)
    