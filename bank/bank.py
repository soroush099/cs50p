def bank(s):
    if s.startswith("hello"):
        print("$0")
    elif s.startswith("h"):
        print("$20")
    else:
        print("$100")

input_user = str(input("Greeting: ")).lower().strip()

bank(input_user)