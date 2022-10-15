from math import pi
def convert():
    print("Choose one:")
    print("1. task")
    print("2. fuck")
    number = input()
    if number not in ("1" , "2"):
        print("ты даун")
    else:
        if number == "1":
            print((11 * (2 ** 2)) - ((13 / 4) + 7))
        elif number == "2":
            print((3 * 36 / (4 * pi)) ** (1/3))
convert()
while True:
    flag = input("One more time? [y/n]: ")

    if flag == 'y':
        convert()
    else:
        break
