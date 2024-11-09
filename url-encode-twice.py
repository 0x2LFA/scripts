import urllib.parse
import sys

# https://stackoverflow.com/questions/67629248/how-do-i-urlencode-all-the-characters-in-a-string-including-safe-characters
def urlencode_all(string):
    return "".join("%{0:0>2x}".format(ord(char)) for char in string)

def urlencode_once(string):
    # URL encode the input string
    return urllib.parse.quote(string)

def main():
    if len(sys.argv) != 2:
        print("Usage: ./urlencodetwice.py <string>")
        sys.exit(1)

    input_string = sys.argv[1]
    
    # Step 1: URL encode the input string, even safe chars
    encoded_once = urlencode_all(input_string)

    # Step 2: URL encode again
    final_encoded = urlencode_once(encoded_once)
    
    print(final_encoded)

if __name__ == "__main__":
    main()

