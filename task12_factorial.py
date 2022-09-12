def factorial(num):
    if num>=2:
        return num*factorial(num-1)
    else:
        return 1
number=int(input("enter a number to be factorial find:"))
result=factorial(number)
print(f"factorial of {number} is",result)