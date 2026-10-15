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


def get_Number(massages):
    while True:
        try:
            return float(input(massages))
        except ValueError:
            print("Please enter valid number")


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % 2 == 0:
            return False
    return True


def show_history():
    if not history:
        print("History is empty.")
        return
    print("\n=====History=====")
    for i, item in enumerate(history, 1):
        print(f"{i} : {item}")


history = []
while True:
    print("--------------------\nWelcome to calculator\n--------------------")
    print(
        "\nBasics\n\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n-----------------\n\nIntermediate\n\n5.Power\n6.Square Root\n7.Factorial\n8.Absloute Root\n-----------------\n\nTrigonometry\n\n9.Sin\n10.Asin\n11.Cos\n12.Acos\n13.Tan\n14.Atan\n15.Cot\n16.Acot\n17.Sinh\n18.Cosh\n19.Tanh\n20.Coth\n-----------------\n\nAdvanced\n\nLogarithm\n\n21.Log\n22.Log10\n23.Log2\n-----------------\n\n24.GCD\n25.LCM\n-----------------\n\n26.E\n27.Pi\n-----------------\n\n28.Prime Check\n-----------------\n\nAbout History\n29.History\n30.Clear history\n31.Exit\n"
    )
    choose = input("Choose one: ")
    if choose == "31":
        print("BYE!")
        break
    if choose == "29":
        show_history()
    elif choose in ["1", "2", "3", "4", "5", "24", "25"]:
        number1 = get_Number("Enter first number: ")
        number2 = get_Number("Enter second number: ")

        if choose == "1":
            result = addition(number1, number2)
            print("Result: ", result)
            history.append(f"{number1} + {number2} = {result}")

        elif choose == "2":
            result = subtract(number1, number2)
            print("Result: ", result)
            history.append(f"{number1} - {number2} = {result}")

        elif choose == "3":
            result = multi(number1, number2)
            print("Result: ", result)
            history.append(f"{number1} * {number2} = {result}")

        elif choose == "4":
            result = division(number1, number2)
            print("Result: ", result)
            history.append(f"{number1} / {number2} = {result}")

        elif choose == "5":
            result = power(number1, number2)
            print("Result: ", result)
            history.append(f"{number1} ^ {number2} = {result}")

        elif choose == "24":
            result = gcd(number1, number2)
            print("Result: ", result)
            history.append(f"GCD ({number1} , {number2})  = {result}")

        elif choose == "25":
            result = lcm(number1, number2)
            print("Result: ", result)
            history.append(f"LCM ({number1} , {number2})   = {result}")

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
        number3 = get_Number("Please enter number: ")
        if choose == "6":
            result = square_root(number3)
            print("Result: ", result)
            history.append(f" √{number3} = {result}")

        elif choose == "7":
            result = fact(number3)
            print("Result: ", result)
            history.append(f" {number3}! = {result}")

        elif choose == "8":
            result = absolute(number3)
            print("Result: ", result)
            history.append(f" √{number3} = {result}")

        elif choose == "9":
            result = sin(number3)
            print("Result: ", result)
            history.append(f" Sin({number3}) = {result}")

        elif choose == "10":
            result = asin(number3)
            print("Result: ", result)
            history.append(f" Arc sin({number3}) = {result}")

        elif choose == "11":
            result = cos(number3)
            print("Result: ", result)
            history.append(f" Cos({number3}) = {result}")

        elif choose == "12":
            result = acos(number3)
            print("Result: ", result)
            history.append(f" Arc cos({number3}) = {result}")

        elif choose == "13":
            result = tan(number3)
            print("Result: ", result)
            history.append(f" Tan({number3}) = {result}")

        elif choose == "14":
            result = atan(number3)
            print("Result: ", result)
            history.append(f" Arc tan({number3}) = {result}")

        elif choose == "15":
            result = cot(number3)
            print("Result: ", result)
            history.append(f" Cot({number3}) = {result}")

        elif choose == "16":
            result = acot(number3)
            print("Result: ", result)
            history.append(f" Arc cot({number3}) = {result}")

        elif choose == "17":
            result = sinh(number3)
            print("Result: ", result)
            history.append(f" Sinh({number3}) = {result}")

        elif choose == "18":
            result = cosh(number3)
            print("Result: ", result)
            history.append(f" Cosh({number3}) = {result}")

        elif choose == "19":
            result = tanh(number3)
            print("Result: ", result)
            history.append(f" Tanh({number3}) = {result}")

        elif choose == "20":
            result = coth(number3)
            print("Result: ", result)
            history.append(f" Coth({number3}) = {result}")

        elif choose == "21":
            result = log(number3)
            print("Result: ", result)
            history.append(f" Log({number3}) = {result}")

        elif choose == "22":
            result = log10(number3)
            print("Result: ", result)
            history.append(f" Log10({number3}) = {result}")

        elif choose == "23":
            result = log2(number3)
            print("Result: ", result)
            history.append(f" Log2({number3}) = {result}")

    elif choose == "28":
        num = get_Number("Please enter number: ")
        if num.is_integer() and is_prime(int(num)):
            result = f"{num} is prime!"
        else:
            result = f"{num} is not prime!"
        history.append(f" is_prime({num}) = {result}")

    elif choose == "26":
        result = math.pi
        print("Pi = ", result)
        history.append(f" Pi = {result}")

    elif choose == "27":
        result = math.e
        print("E = ", result)
        history.append(f" E = {result}")

    elif choose == "30":
        history.clear()
        print("History cleared!")
