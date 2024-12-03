def Math(s):

    x, y, z = s.split(" ")

    namber1 = float(x)
    namber2 = float(z)

    if y == "+":
        namber3 = namber1+namber2
        print(f"{namber3:.1f}")
    if y == "-":
        namber3 = namber1-namber2
        print(f"{namber3:.1f}")
    if y == "/":
        namber3 = namber1/namber2
        print(f"{namber3:.1f}")
    if y == "*":
        namber3 = namber1*namber2
        print(f"{namber3:.1f}")

input_user = input("Expression: ").strip()
Math(input_user)