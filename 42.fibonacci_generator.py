def fibo(num):
    a = 0
    b = 1
    for x in range(num):
        yield a
        temp = a
        a = b
        b = temp+b


for x in fibo(10):
    print(x)

# using list


def list_fibo(num):
    a = 0
    b = 1
    result_list = []
    for x in range(num):
        result_list.append(a)
        temp = a
        a = b
        b = temp+b
    return result_list


print(list_fibo(10))
