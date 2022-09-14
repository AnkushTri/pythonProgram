# Write a Python program to convert temperatures to and from Celsius, Fahrenheit. 
# [ Formula: c/5 = f-32/9] 
print("enter 1 for Celsius to f and 2 for fehrenheit to celsius")
over=False

#celsius to fahrenheit
while(over!=True):
    temp = input("enter your choice:")

    if temp=="1":
    
        cel=int(input("enter tempreture in celsius:"))
        fah=(cel*9/5)+32
        print("tempretures in fahernheit is",fah)
        over=True


    #fahrenheit to celsius
    elif temp=="2":
        fah =int(input("enter temperature in fahrenheit:"))
        cel=(fah-32)*5/9
        print("Tempretures in celsius is",cel)
        over = True


    else:
        print("Please,enter valid choice")
        over = False



