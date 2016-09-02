
def fak(n):
    if n==1:
        return 1;
    else:
        return n * fak(n-1);


def fib(n):
    if n<=2:
        return 1;
    else:
        return fib(n-1)+fib(n-2);

print fib(4)