def fibo_recursive(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)


def fibo_iterative(n):
    a, b = 0, 1
    if n == 1:
        return a
    elif n == 2:
        return b
    while n - 2 > 0:
        c = a + b
        a, b = b, c
        n = n - 1
    return c


num = int(input("Enter the number of fibonacci numbers required : "))
iterative, recursive = [], []
for i in range(1, num+1):
    iterative.append(str(fibo_iterative(i)))
    recursive.append(str(fibo_recursive(i)))
print('Iterative: ' + ' '.join(iterative))
print('Recursive: ' + ' '.join(recursive))
