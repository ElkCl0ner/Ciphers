from string import ascii_letters

key = "LDOMqnPvrxGywQhaXcTdklBifVjKRzuWebSmUAgCIYtpHsZFNoEJ"

def _display_menu():
    print("Would you like to encode or decode a message?")

def encode(msg):
    out = ""

    for letter in msg:
        if letter in ascii_letters:
            out += key[ascii_letters.find(letter)]
        else:
            out += letter

    return out

def decode(msg):
    out = ""

    for letter in msg:
        if letter in ascii_letters:
            out += ascii_letters[key.find(letter)]
        else:
            out += letter

    return out

while True:

    _display_menu()
    userIn = input()

    if userIn == "exit":
        break

    elif userIn == "encode":
        print("What is the message to encode?")
        msg = input()
        print("The encoded message is:\n{}".format(encode(msg)))

    elif userIn == "decode":
        print("What is the message to decode?")
        msg = input()
        print("The decoded message is:\n{}".format(decode(msg)))
