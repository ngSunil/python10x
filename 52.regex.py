import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
teststring = 'a'
try:
    re.fullmatch(regex, teststring).span()
except AttributeError as err:
    print(f'Something went wrong {err}')
# password checker
regex_pwd = r'[a-zA-Z0-9#$]{8,}\d$'
try:
    re.fullmatch(regex_pwd, input('Please enter the password: ')).span()
    print('Strong Password')
except AttributeError as err:
    print(f'Not as required password')

pattern = r'[a-zA-Z0-9#$]{8,}\d$'
text = "Abcd1234$9"

if re.match(pattern, text):
    print("Match found")
else:
    print("No match")
