#!/usr/bin/python3
def unicode_encode(input_string):
    # Encode each character in the string to its Unicode representation
    unicode_encoded = ''.join(f'\\u{ord(char):04x}' for char in input_string)
    return unicode_encoded

if __name__ == "__main__":
    # Get user input
    user_input = input("Enter a string to encode in Unicode: ")
    encoded_string = unicode_encode(user_input)
    print(f"Unicode encoded string: {encoded_string}")

