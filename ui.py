def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def modulus(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x % y

def exponent(x, y):
    return x ** y

def calculator():
    print("=== Welcome to the Modern Calculator ===")

    operations = {
        '1': ('Add (+)', add),
        '2': ('Subtract (-)', subtract),
        '3': ('Multiply (*)', multiply),
        '4': ('Divide (/)', divide),
        '5': ('Modulus (%)', modulus),
        '6': ('Exponentiation (^)', exponent),
        'q': ('Quit', None)
    }

    while True:
        print("\nSelect operation:")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")

        choice = input("Enter choice: ").strip().lower()

        if choice == 'q':
            print("Thanks for using the calculator! Goodbye.")
            break

        if choice not in operations:
            print("Invalid choice! Please select a valid operation.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        operation_func = operations[choice][1]
        result = operation_func(num1, num2)

        print(f"Result: {result}")

if __name__ == "__main__":
    calculator()
