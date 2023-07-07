import sys
import random
input_no = sys.argv[1]
random_no = random.randint(1, 3)
print(random_no)
if int(input_no) == random_no:
    print('You are a genuius')
