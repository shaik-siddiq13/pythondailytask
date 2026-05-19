def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"


while True:
    print("\n--- SIMPLE CALCULATOR ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Exiting calculator. Thank you!")
        break

    if choice in ['1', '2', '3', '4']:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == '1':
            print("Result =", add(a, b))
        elif choice == '2':
            print("Result =", sub(a, b))
        elif choice == '3':
            print("Result =", mul(a, b))
        elif choice == '4':
            print("Result =", div(a, b))
    else:
        print("Invalid choice! Please select 1-5.")