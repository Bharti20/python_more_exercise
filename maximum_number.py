def my_function():
    number1=int(input("inter the number"))
    number2=int(input("inter the number"))
    number3=int(input("inter the number"))
    if number1==number2==number3:
        print("equal hai")
    elif number1>number2 and number1>number3:
        print(number1,"greater")
    elif number2>number1 and number2>number3:
        print(number2,"greater")
    else:
        print(number3,"greater")
my_function()