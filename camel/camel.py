def camell(h):
    print("snake_case: ",end="")
    for s in h:
        if s.islower():
            print(s, end="")
        if s.isupper():
            print("_", s.lower(), end="", sep="")
    print()

input_user = input("camelCase: ")
camell(input_user)