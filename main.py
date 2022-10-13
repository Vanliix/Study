def convert():
    print("Choose one:")
    print("1. task")
    number = input()
    if number not in ("1"):
        print("ты даун")
    else:
        if number == "1":
            print((11 * (2 ** 2)) - ((13 / 4) + 7))

convert()
while True:
    flag = input("One more time? [y/n]: ")

    if flag == 'y':
        convert()
    else:
        break
