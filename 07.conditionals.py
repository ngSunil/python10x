age = 18
if age < 10:
    print('Too young')
elif age == 10:
    print('Try this year')
else:
    print(' Take the car keys')
# we can have multiple elif but only one if and else
# also mind the spaces there will be 4 spaces

# TRUTHY VS FALSEY
print(bool(5), bool(''), bool(0))

# TERNARY OPERATOR
is_friend = True
can_message = "message allowed" if is_friend else "message not allowed"
print(can_message)

# SHORT CIRCUITING
a = True
b = True
if a or b:  # that means In or statement if first one is true it need not look after beyondf other condition, it simply short circuits and skips  same for False in and
    print('ok')

#  LOGICAL OPERATORS
# ><
is_magician = False
is_expert = True
if is_magician and is_expert:
    print('You are a master magician')
elif is_magician and not is_expert:
    print('at least you are getting there')
elif not is_magician:
    print('You need magic powers')

# Difference between is and ==
