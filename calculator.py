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


def log10(a):
    return math.log10(a)


def log2(a):
    return math.log2(a)


def sinh(a):
    return math.sinh(a)


def cosh(a):
    return math.cosh(a)


def tanh(a):
    return math.cosh(a)


def coth(a):
    return 1 / math.tan(a)


def gcd(a, b):
    return math.gcd(int(a), int(b))


def lcm(a, b):
    return math.lcm(int(a), int(b))


while True:
    print("--------------------\nWelcome to calculator\n--------------------")
    print(
        "Basics\n\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n\n\n5.Power\n6.Square Root\n7.Factorial\n8.Absloute Root\n\n\n9.Sin\n10.Asin\n11.Cos\n12.Acos\n13.Tan\n14.Atan\n15.Cot\n16.Acot\n17.Sinh\n18.Cosh\n19.Tanh\n20.Coth\n\n21.Log\n22.Log10\n23.Log2\n\n24.GCD\n25.LCM\n\n26.E\n27.Pi\n\n\n28.Exit"
    )
    choose = input("Choose one: ")
    if choose == "28":
        print("BYE!")
        break
    elif choose in ["1", "2", "3", "4", "5", "24", "25"]:
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
        elif choose == "24":
            print("Result: ", gcd(number1, number2))
        elif choose == "25":
            print("Result: ", lcm(number1, number2))
        

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
        "20",
        "21",
        "22",
        "23",
    ]:
        number3 = float(input("Enter the number: "))
        if choose == "6":
            print("Result: ", square_root(number3))
        elif choose == "7":
            print("Result: ", fact(number3))
        elif choose == "8":
            ("Result: ", absolute(number3))
        elif choose == "9":
            print("Result: ", sin(number3))
        elif choose == "10":
            print("Result: ", asin(number3))
        elif choose == "11":
            print("Result: ", cos(number3))
        elif choose == "12":
            print("Result: ", acos(number3))
        elif choose == "13":
            print("Result: ", tan(number3))
        elif choose == "14":
            print("Result: ", atan(number3))
        elif choose == "15":
            print("Result: ", cot(number3))
        elif choose == "16":
            print("Result: ", acot(number3))
        elif choose == "17":
            print("Result: ", sinh(number3))
        elif choose == "18":
            print("Result: ", cosh(number3))
        elif choose == "19":
            print("Result: ", tanh(number3))
        elif choose == "20":
            print("Result: ", coth(number3))
        elif choose == "21":
            print("Result: ", log(number3))
        elif choose == "22":
            print("Result: ", log10(number3))
        elif choose == "23":
            print("Result: ", log2(number3))
    elif choose == "26":
        print("Pi = ", math.pi)
    elif choose == "27":
        print("E = ", math.e)
