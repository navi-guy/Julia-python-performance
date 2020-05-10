#Fibonacci
# Complejidad O(n)

def fibonacciPython(n):
    t1 = 0
    t2 = 1
    nextTerm = 0

    for x in range(1,n):
        if x == 1:
            t1
        elif x == 2:
            t2

        nextTerm = t1 + t2
        t1 = t2
        t2 = nextTerm

fibonacciPython(5000)

