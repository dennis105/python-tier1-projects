def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        return None


def show_menu():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit")

while True:
    show_menu()

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Quitting...")
        break

    if choice not in [1, 2, 3, 4, 5]:
        print("Invalid choice")
        continue

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == 1:
        result = add(a, b)
        print(f"Result: {result}")
    elif choice == 2:
        result = subtract(a, b)
        print(f"Result: {result}")
    elif choice == 3:
        result = multiply(a, b)
        print(f"Result: {result}")
    elif choice == 4:
        result = divide(a, b)

        if result is None:
            print("Cannot divide by zero.")
        else:
            print(f"Result: {result}")