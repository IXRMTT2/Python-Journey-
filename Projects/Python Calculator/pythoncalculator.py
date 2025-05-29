import math

def calculator():
    global result
    print("Enhanced Calculator")
    print("Supported operations:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exponentiation (^ or **)")
    print("6. Modulus (%)")
    print("7. Floor Division (//)")
    print("8. Square Root (sqrt)")
    print("9. Logarithm (log base 10)")
    print("10. Natural Logarithm (ln)")
    print("11. Sine (sin)")
    print("12. Cosine (cos)")
    print("13. Tangent (tan)")
    print("14. Factorial (!)")
    print("Type 'quit' to quit.")

    while True:
        op = input("\nEnter operation symbol (e.g., +, -, *, /, ^, sqrt, sin, !): ").strip().lower()

        if op == 'quit':
            print("Ciao!")
            break

        if op in ('sqrt', 'log', 'ln', 'sin', 'cos', 'tan', '!'):
            try:
                num = float(input("Enter the number: "))
            except ValueError:
                print("Invalid. Try again.")
                continue

            if op == 'sqrt':
                if num < 0:
                    print("Whoops: Cannot take square root of negative number.")
                    continue
                result = math.sqrt(num)

            elif op == 'log':
                if num <= 0:
                    print("Whoops: Logarithm undefined for non-positive numbers.")
                    continue
                result = math.log10(num)

            elif op == 'ln':
                if num <= 0:
                    print("Whoops: Natural logarithm undefined for non-positive numbers.")
                    continue
                result = math.log(num)

            elif op == 'sin':
                result = math.sin(math.radians(num))

            elif op == 'cos':
                result = math.cos(math.radians(num))

            elif op == 'tan':
                rad = math.radians(num)
                if math.isclose(math.cos(rad), 0, abs_tol=1e-9):
                    print("Whoops: Tangent undefined at this angle.")
                    continue
                result = math.tan(rad)

            elif op == '!':
                if not num.is_integer() or num < 0:
                    print("Whoops: Factorial only defined for non-negative integers.")
                    continue
                result = math.factorial(int(num))

            print(f"{op}({num}) = {result}")

        elif op in ('+', '-', '*', '/', '^', '**', '%', '//'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid. Try again.")
                continue

            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                if num2 == 0:
                    print("Whoops: Division by zero (aint possible with a calculator, are you kidding?).")
                    continue
                result = num1 / num2
            elif op in ('^', '**'):
                result = num1 ** num2
            elif op == '%':
                if num2 == 0:
                    print("Error: Modulus by zero.(aint possible with a calculator, are you kidding?).")
                    continue
                result = num1 % num2
            elif op == '//':
                if num2 == 0:
                    print("Error: Floor division by zero.(aint possible with a calculator, are you kidding?).")
                    continue
                result = num1 // num2

            print(f"{num1} {op} {num2} = {result}")

        else:
            print("Unsupported. Please try again.")

if __name__ == "__main__":
    calculator()
