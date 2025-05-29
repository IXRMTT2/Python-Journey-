def caesar_cipher(text, shift, mode='encode'):

    result = []

    if mode == 'decode':
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            offset = (ord(char) - base + shift) % 26
            result.append(chr(base + offset))
        else:
            result.append(char)

    return ''.join(result)


def main():
    print("Caesar Cipher Tool")
    while True:
        mode = input("Type 'encode' to encrypt, 'decode' to decrypt, or 'q' to quit: ").lower()
        if mode == 'q':
            print("Cya later buckeroo")
            break
        if mode not in ('encode', 'decode'):
            print("Large red button.mp4 (get it)")
            continue

        text = input("Enter your message: ")
        try:
            shift = int(input("Enter shift number (e.g. 3): "))
        except ValueError:
            print("Large red button.mp4 (get it)")
            continue

        transformed = caesar_cipher(text, shift, mode)
        print(f"Result: {transformed}\n")


if __name__ == "__main__":
    main()
