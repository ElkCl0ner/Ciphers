def _display_menu():
    print("Would you like to encode or decode a message?")

def encode(msg, key):
    out = ""

    leng = len(msg)

    cypherText = []

    for pos in range(key):
        cypherText.append([])
        ind = pos
        while True:
            if pos == 0 or pos == key - 1:
                cypherText[pos].append(msg[ind])
                ind += 2 + 2 * (key - 2)
                if ind >= leng:
                    break

            else:
                cypherText[pos].append(msg[ind])
                ind += 2 + 2 * (key - 2) - 2 * pos
                if ind >= leng:
                    break
                cypherText[pos].append(msg[ind])
                ind += 2 * pos
                if ind >= leng:
                    break

    for rail in cypherText:
        for char in rail:
            out += char

    return out

def decode(msg, key):
    out = ""

    rails = []

    lengs = []
    leng = len(msg)

    for pos in range(key):
        lengs.append(int(leng / (2 + 2 * (key - 2))))
        if not (pos == 0 or pos == key - 1):
            lengs[pos] *= 2

    if leng % (2 + 2 * (key - 2)) >= key:
        for pos in range(key):
            lengs[pos] += 1
        if leng % (2 + 2 * (key - 2)) != key:
            for pos in range(key - 2, key - 2 - leng % (2 + 2 * (key - 2)) + key, - 1):
                lengs[pos] += 1
    else:
        for pos in range(leng % (2 + 2 * (key - 2))):
            lengs[pos] += 1

    for leng_ in lengs:
        rails.append(msg[0:leng_])
        msg = msg[leng_:]

    plainText = []

    for rail in rails:
        temp = []
        for ch in rail:
            temp.append(ch)
        plainText.append(temp)

    stop = False
    while True:
        for pos in range(key):
            if len(plainText[pos]) == 0:
                stop = True
                break
            out += plainText[pos].pop(0)
        if stop:
            break

        for pos in range(key - 2, 0, - 1):
            if len(plainText[pos]) == 0:
                stop = True
                break
            out += plainText[pos].pop(0)
        if stop:
            break

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
