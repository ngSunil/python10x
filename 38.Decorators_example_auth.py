# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    # changing this will either run or not run the message_friends function.
    'valid': True
}


def authenticated(fn):
    # code here
    def check_uservalidity(*args, **kwargs):
        print(args[0]['valid'])
        if args[0]['valid']:
            return fn(*args, **kwargs)
        # message_friends(args[0])
    return check_uservalidity


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
