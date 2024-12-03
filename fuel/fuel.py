def def1():
    while True:
        try:
            while True:
                input_user = input("Fraction: ")
                x , y = input_user.split("/")
                x = int(x)
                y = int(y)
                if y >= 0 and x <= y:
                    break
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        else:
            break
    return x , y

x , y = def1()

a = int(round((x/y)*100))
if a >= 99:
    print("F")
elif a <= 1:
    print("E")
else:
    print(f"{a}%")