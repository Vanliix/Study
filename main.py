def convert():
    print("Choose one:")
    print("1. calc")
    print("2. pornhub.com")
    number = input()
    if number in ("1"):
        print("enter digits: ")
        a = int(input())
        b = int(input())
        x = input("pohui:")
        if x == "+":
            print(a+b)
        elif x == "-":
            print(a-b)
        elif x == "*":
            print(a*b)
        elif x == "/":
            print(a/b)
        else:
            if a:
                print(a/b)
            else:
                print("ПОШЕЛ ТЫ НАХУЙ!")
    else:
        print("пошел ты нахуй!")


convert()
while True:
    flag = input("One more time? [y/n]: ")

    if flag == 'y':
        convert()
    else:
        break
