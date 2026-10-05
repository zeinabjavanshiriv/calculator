


def addition(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multi(a, b):
    return a * b


def division(a, b):
    if a == 0:
        return "Can't divid with zero"
    return a / b


while True:
    print("--------------------\nWelcome to calculator\n--------------------")
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
    choose = input("Choose one: ")
    if choose == "5":
        print("BYE!")
        break
    if choose in ["1","2","3","4"]:
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        if choose == "1":
            print("Result: ", addition(number1,number2))
        elif choose == "2":
                    print("Result: ", subtract(number1,number2))
        elif choose == "3":
                    print("Result: ", multi(number1,number2))
        elif choose == "4":
                    print("Result: ", division(number1,number2))

