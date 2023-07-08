import random
input_no = input('Please enter a number between 1~4 ')


def match_no(input_no):
    random_no = random.randint(1, 3)
    print(random_no)
    if (int(input_no) not in range(1, 10)):
        print('Input not in rnage 1-10')
        return False
    if int(input_no) == random_no:
        return True
    else:
        return False


while True:
    if match_no(input_no):
        print('Right Gues')
        break
    else:
        input_no = input('Please enter a number between 1~4 ')
        match_no(input_no)
