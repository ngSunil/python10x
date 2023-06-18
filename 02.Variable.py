# Snake case
# Start with lower case or underscore
# case sensitive
# Dont overwrite keywords
# CONTANTS ALL CAPS LIE
PI = 3.141
# contants should not be changed
# You can also use belwo for assigning multiple vars in one statements
a, b, c = 1, 2, 3
# expressions are those that produces a value
b = 10
a = b/2  # 9/2 is an expresion and the entire line is an statement
# augmented assignment operator
a += 2
print(a)
# strings
# can be '' or double ""
# but for multiple lines use rthree ''' eg
a = '''
WOW
0 0 
 _
'''
print(a)
# YOU CANALSO ADD MULTIPLE STRING TOGTEHR
var1, var2 = 'a', 'b'
print(var1+var2)

# type conversion
print(str(100))  # 100 is now a string
# escape sequence \ tells python to think that everything that comes after the \ shall be a string
print('It\'s raining outside \"sasa\"')
# \t will add a tab
# \n shows a new line
# Formatted String otherwise we will have to keep on using + to concatenate strings
# somebody uses .format aftet the =string AND it was in pythion 2
name, age = 'Sunil', 35
print(f'Hi! {name} and you are {age} years old')
# String index
string = 'Python'
print(string[0])
print(string[0:5:2])  # [start:stop:step]
print(string[:5], string[5:])
print(string[-2])  # start from the end of the string
print(string[::-1])  # reverser the string
print(string[::-2])  # reverser the string skip 2
# Strings are immutable because
# string[0] = 'C'
# Built in functions and methods
print(len('Hello'))
print(string[0: len(string)-3])
print(string.upper())
print(string.capitalize())
print(string.find('th'))
print(string.replace('t', 'g'))

# BOOLEANS
print(bool(1))
is_loading = True
print(is_loading)

# assignment age
year_birth = input('What year were you born?')
print(f'your age is {2023-int(year_birth)}')
# Comments
# Only comment where the code is abit complex unnecessary  commenting where variable names only show what is happening is useless
# assignment password checker
username = input('What is your username? ')
password = input('Enter your password')
passd = '*' * len(password)
print(f'Hello {username}!. Your password {passd} is {len(password)} long!')
