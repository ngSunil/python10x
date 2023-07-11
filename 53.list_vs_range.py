from time import time

x1 = time()
print(sum(list(range(1, 999999))))
diff = time() - x1
print(f'{diff:0.7f}')

x1 = time()
print(sum(range(1, 999999)))
diff = time() - x1
print(f'{diff:0.7f}')
