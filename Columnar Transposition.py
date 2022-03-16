userIn = int(input("factorial"))

x = [userIn,1]

while True:
    if x[0] == 1:
        print(x[1])
        break
    else:
        x[1] *= x[0]
        x[0] -= 1