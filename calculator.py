import math


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


def power(a, b):
    return math.pow(a, b)


def square_root(a):
    if a < 0:
        return "can't calculate the negative numbers"
    return math.sqrt(a)


def fact(a):
    if a < 0 or not a.integer():
        return "Fact needs non-negative numbers"
    return math.factorial(int(a))


def absolute(a):
    return math.fabs(a)


def round_up(a):
    return math.ceil(a)


def round_down(a):
    return math.floor(a)


def sin(a):
    return math.sin(math.radians(a))


def asin(a):
    return math.degrees(math.asin(a))


def cos(a):
    return math.cos(math.radians(a))


def acos(a):
    return math.degrees(math.acos(a))


def tan(a):
    return math.tan(math.radians(a))


def atan(a):
    return math.degrees(math.atan(a))


def cot(a):
    return 1 / math.tan(math.radians(a))


def acot(a):
    return math.degrees(math.atan(1 / a))


def log(a):
    return math.log(a)


while True:
    print("--------------------\nWelcome to calculator\n--------------------")
    print(
        "1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Power\n6.Square Root\n7.Factorial\n\n8.Sin\n9.Asin\n10.Cos\n11.Acos\n12.Tan\n13.Atan\n14.Cotan\n15.Acotan\n\n16.Log\n\n17.Absoulute value\n18.round up\n19.Round down\n\n20.Sinh\n21.Cosh\n22.Tanh\n23.Coth\n\n\n25.Exit\n"
    )
    choose = input("Choose one: ")
    if choose == "20":
        print("BYE!")
        break
    elif choose in ["1", "2", "3", "4", "5"]:
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        if choose == "1":
            print("Result: ", addition(number1, number2))
        elif choose == "2":
            print("Result: ", subtract(number1, number2))
        elif choose == "3":
            print("Result: ", multi(number1, number2))
        elif choose == "4":
            print("Result: ", division(number1, number2))
        elif choose == "5":
            print("Result: ", power(number1, number2))
    elif choose in [
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
    ]:
        number3 = float(input("Enter the number: "))
        if choose == "6":
            print("Result: ", square_root(number3))
        elif choose == "7":
            print("Result: ", fact(number3))
        elif choose == "8":
            print("Result: ", sin(number3))
        elif choose == "9":
            print("Result: ", asin(number3))
        elif choose == "10":
            print("Result: ", cos(number3))
        elif choose == "11":
            print("Result: ", acos(number3))
        elif choose == "12":
            print("Result: ", tan(number3))
        elif choose == "13":
            print("Result: ", atan(number3))
        elif choose == "14":
            print("Result: ", cot(number3))
        elif choose == "15":
            print("Result: ", acot(number3))
        elif choose == "16":
            print("Result: ", log(number3))
        elif choose == "17":
            print("Result: ", absolute(number3))
        elif choose == "18":
            print("Result: ", round_up(number3))
        elif choose == "19":
            print("Result: ", round_down(number3))
