from string import ascii_lowercase as alpha
from string import ascii_letters as letters

def _display_menu():
    print("Would you like to encode or decode a message?")

def encode(msg, key):
    out = ""

    alpha1 = ""
    for pos in range(26):
        alpha1 += alpha[(pos + key) % 26]

    alpha2 = alpha1.upper()

    alpha3 = alpha1 + alpha2

    for char in msg:
        if char in alpha3:
            pos = letters.find(char)
            out += alpha3[pos]

        else:
            out += char

    return out

def decode(msg, key):
    out  = ""

    alpha1 = ""
    for pos in range(26, 52):
        alpha1 += alpha[(pos - key) % 26]

    alpha2 = alpha1.upper()

    alpha3 = alpha1 + alpha2

    for char in msg:
        if char in alpha3:
            pos = letters.find(char)
            out += alpha3[pos]

        else:
            out += char

    return out

while True:
    _display_menu()
    userIn = input()

    if userIn == "exit":
        break

    if userIn == "encode":
        print("What is the message to encode?")
        msg = input()
        print("What is the encoding key?")
        key = int(input())

        print("The encoded message is:\n{}".format(encode(msg, key)))

    if userIn == "decode":
        print("What is the message to decode?")
        msg = input()
        print("What is the decoding key?")
        key = int(input())

        print("The decoded message is:\n{}".format(decode(msg, key)))
