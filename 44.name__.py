from test100.test1 import hello
print(__name__)
print(hello())
if __name__ == '__main__':
    print('I had to run')
# if __name__ == '__main__' that means it is the first file that has been executed
# so this if is used to identify and only run the code below if the name of the file is __main__
