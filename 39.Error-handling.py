# Error handling allows python code to keep running even if something goes wrong
# Syntax error
li = [1, 2]
# print(li[10])

while True:
    try:
        age = input('Please enter your age?')
        x = int(age)
        100/x
        if x > 150:
            # you can raise your own exception
            raise Exception('hey age cannot be greater than 150')
        print(f'you are {x} years old')
    except ValueError as err:
        print(f"Print  please enter an integer \n {err}")
    except ZeroDivisionError:
        print('Please enter age higher than 0')
    else:
        print('Thank you')
        break
    finally:
        print('ok, I am finally done')
