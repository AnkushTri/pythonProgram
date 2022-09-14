
def fibonacci(n):
    a=0
    b=1
    print(a, end=" ")
    for i in range (n-1):
        c=a+b
        print(c , end=" ")
        a=b
        b=c