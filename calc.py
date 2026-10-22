
def add(a,b):
    return a+b
def subtract(a,b)
    return a-b

def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

def main():
    while True:
        a = float(input("First number: "))
        op = input("Operator (+ - * /): ")
        b = float(input("Second number: "))
        if op == "+":
            print("Result:", add(a, b))
        elif op == "-":
            print("Result:", subtract(a, b))
        elif op == "*":
            print("Result:", multiply(a, b))
        elif op == "/":
            print("Result:", divide(a, b))
        else:
            print("Unknown operator:", op)
if __name__ == "__main__":
    main()