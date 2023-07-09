def fibonacci(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    else:
        return fibonacci(a-2) + fibonacci(a-1)
for a in range(10):
    print(fibonacci(a))
