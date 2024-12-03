input_user = str(input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")).strip().lower()

listbax = ["42", "forty-two", "forty two"]

if input_user in listbax:
    print("Yes")
else:
    print("No")
