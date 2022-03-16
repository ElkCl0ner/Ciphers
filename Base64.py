import string

table = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'

def _display_menu():
    print("Would you like to encode or decode a message?")

def encode(msg, iterations):
    out = ""

    ascii_ints = [ord(char) for char in msg]

    binary = ""
    for ascii_int in ascii_ints:
        binary += format(ascii_int, "b").zfill(8)

    while True:
        if len(binary) < 6:
            if len(binary) == 0:
                break
            else:
                fillers = 6 - (len(binary) % 6)
                binary += "0" * fillers
                out += table[int(binary[:6], 2)]
                out += "=" * int(0.5 * fillers)
                break
        else:
            out += table[int(binary[:6], 2)]
            binary = binary[6:]

    if iterations > 1:
        return encode(out, iterations - 1)
    else:
        return out

def decode(msg, iterations):
    out = ""
    fillers = 0

    while True:
        if msg[-1] == "=":
            fillers += 1
            msg = msg[:-1]
        else:
            break

    table_ints = [table.find(char) for char in msg]

    binary = ""
    for table_int in table_ints:
        binary += format(table_int, "b").zfill(6)

    for _ in range(fillers):
        binary = binary[:-2]

    while True:
        if not binary:
            break

        out += chr(int(binary[:8], 2))
        binary = binary[8:]

    if iterations > 1:
        return decode(out, iterations - 1)
    else:
        return out

while True:
    _display_menu()
    userIn = input()

    if userIn == "exit":
        break

    if userIn == "encode":
        print("What is the message to encode?")
        msg = input()
        print("How many iterations?")
        iterations = int(input())

        print("The encoded message is:\n{}".format(encode(msg, iterations)))

    if userIn == "decode":
        print("What is the message to decode?")
        msg = input()
        print("How many iterations?")
        iterations = int(input())

        print("The decoded message is:\n{}".format(decode(msg, iterations)))
