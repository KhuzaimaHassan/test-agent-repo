import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Division by zero is undefined.")
    return x / y

def power(base, exponent):
    try:
        return math.pow(base, exponent)
    except OverflowError:
        raise ValueError("Result is too large (Overflow Error).")

def square_root(x):
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(x)

def log_base_10(x):
    if x <= 0:
        raise ValueError("Logarithm is undefined for non-positive values.")
    return math.log10(x)

def natural_log(x):
    if x <= 0:
        raise ValueError("Natural logarithm is undefined for non-positive values.")
    return math.log(x)

def sine(x, degrees=True):
    val = math.radians(x) if degrees else x
    return math.sin(val)

def cosine(x, degrees=True):
    val = math.radians(x) if degrees else x
    return math.cos(val)

def tangent(x, degrees=True):
    val = math.radians(x) if degrees else x
    # Tangent is undefined where cosine is 0
    if math.isclose(math.cos(val), 0.0, abs_tol=1e-9):
        raise ValueError("Tangent is undefined for this angle.")
    return math.tan(val)

def factorial(x):
    if x < 0:
        raise ValueError("Factorial of a negative number is undefined.")
    if not x.is_integer():
        raise ValueError("Factorial is only defined for integers.")
    return math.factorial(int(x))

def display_menu():
    print("\n" + "="*40)
    print("         SCIENTIFIC CALCULATOR")
    print("="*40)
    print("1.  Addition (+)")
    print("2.  Subtraction (-)")
    print("3.  Multiplication (*)")
    print("4.  Division (/)")
    print("5.  Power (x^y)")
    print("6.  Square Root (\u221ax)")
    print("7.  Logarithm (Base 10)")
    print("8.  Natural Logarithm (ln)")
    print("9.  Sine (sin)")
    print("10. Cosine (cos)")
    print("11. Tangent (tan)")
    print("12. Factorial (!)")
    print("13. Exit")
    print("="*40)

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid numerical value.")

def main():
    while True:
        display_menu()
        choice = input("Enter selection (1-13): ").strip()
        
        if choice == '13':
            print("Thank you for using Scientific Calculator. Goodbye!")
            break
            
        if choice not in [str(i) for i in range(1, 14)]:
            print("Invalid selection. Please choose a valid option (1-13).")
            continue
            
        try:
            if choice in ['1', '2', '3', '4', '5']:
                # Two operand calculations
                num1 = get_float_input("Enter first number: ")
                num2 = get_float_input("Enter second number: ")
                
                if choice == '1':
                    print(f"\nResult: {num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"\nResult: {num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"\nResult: {num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"\nResult: {num1} / {num2} = {divide(num1, num2)}")
                elif choice == '5':
                    print(f"\nResult: {num1} ^ {num2} = {power(num1, num2)}")
                    
            elif choice in ['6', '7', '8', '12']:
                # One operand calculations
                num = get_float_input("Enter number: ")
                
                if choice == '6':
                    print(f"\nResult: \u221a{num} = {square_root(num)}")
                elif choice == '7':
                    print(f"\nResult: log10({num}) = {log_base_10(num)}")
                elif choice == '8':
                    print(f"\nResult: ln({num}) = {natural_log(num)}")
                elif choice == '12':
                    print(f"\nResult: {int(num)}! = {factorial(num)}")
                    
            elif choice in ['9', '10', '11']:
                # Trigonometric operations
                num = get_float_input("Enter angle value: ")
                unit = input("Is the angle in (D)egrees or (R)adians? (D/R): ").strip().upper()
                while unit not in ['D', 'R']:
                    unit = input("Invalid input. Enter 'D' for Degrees or 'R' for Radians: ").strip().upper()
                
                is_degrees = (unit == 'D')
                unit_str = "degrees" if is_degrees else "radians"
                
                if choice == '9':
                    print(f"\nResult: sin({num} {unit_str}) = {sine(num, is_degrees)}")
                elif choice == '10':
                    print(f"\nResult: cos({num} {unit_str}) = {cosine(num, is_degrees)}")
                elif choice == '11':
                    print(f"\nResult: tan({num} {unit_str}) = {tangent(num, is_degrees)}")
                    
        except ValueError as e:
            print(f"\nCalculation Error: {e}")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")
            
        input("\nPress Enter to return to menu...")

if __name__ == '__main__':
    main()
