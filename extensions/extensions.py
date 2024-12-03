def Type(s):
    a = s.rfind(".")
    filetype = s[a:]

    if filetype == ".gif":
        print("image/gif")
    elif filetype ==".jpg":
        print("image/jpeg")
    elif filetype ==".jpeg":
        print("image/jpeg")
    elif filetype ==".png":
        print("image/png")
    elif filetype ==".pdf":
        print("application/pdf")
    elif filetype ==".txt":
        print("text/plain")
    elif filetype ==".zip":
        print("application/zip")
    else:
        print("application/octet-stream")

input_user = input("File name: ").strip().lower()
Type(input_user)