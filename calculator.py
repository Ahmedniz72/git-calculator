def add(a,b):
    return a + b


def subtract(a, b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a, b):
    if b == 0:
        return "ERROR: Division by zero"
    return a / b
def modulo(a, b):
    return a % b

def power(a, b):
    return a ** b


print("Simple Calculator")
print("5+3 = ", add(5,3))
print("23-2 = ",subtract(23,2))
print("6 * 7 =", multiply(6, 7))
print("20 / 5 =", divide(20, 5))
print("10 % 3 =", modulo(10, 3))
print("2 ^ 3 =", power(2, 3))

