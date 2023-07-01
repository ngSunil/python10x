from time import time


def range_perf():
    t1 = time()
    for x in range(100000000):
        x*3
    diff = time() - t1
    print(f"{diff: 0.16f}")


def list_perf():
    t1 = time()
    for x in list(range(100000000)):
        x*3
    diff = time() - t1
    print(f"{diff: 0.16f}")


range_perf()
list_perf()
