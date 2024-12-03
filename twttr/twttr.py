def main(a):
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    print("Output: ",end="")
    for s in input_user:
        if s.lower() not in vowels:
            print(s , end="")
    print()

input_user = input("Input: ")
main(input_user)