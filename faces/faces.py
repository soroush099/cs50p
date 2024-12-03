def main():
    in_user = input(" = ")
    print(convert(in_user))

def convert(in_user):
    a = in_user.replace(":(", "🙁").replace(":)", "🙂")
    return a

main()