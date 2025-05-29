def camel_to_snake_loop(s):
    result = ""
    for char in s:
        if char.isupper():
            if result:
                result += "_"
            result += char.lower()
        else:
            result += char
    return result

def camel_to_snake_lc(s):
    chars = [('_' + c.lower()) if c.isupper() and i != 0 else c.lower()
             for i, c in enumerate(s)]
    return "".join(chars)

def main():
    print("CamelCase / PascalCase to snake_case Converter")
    while True:
        print("\nChoose method:")
        print("1 - For loop")
        print("2 - List comprehension")
        print("quit - Quit")
        choice = input("Your choice: ").strip().lower()

        if choice == 'quit':
            print("Buh bye")
            break
        elif choice in ('1', '2'):
            text = input("Enter CamelCase or PascalCase string: ").strip()
            if choice == '1':
                result = camel_to_snake_loop(text)
            else:
                result = camel_to_snake_lc(text)
            print(f"snake_case result: {result}")
        else:
            print("Invalid, try again.")

if __name__ == "__main__":
    main()
