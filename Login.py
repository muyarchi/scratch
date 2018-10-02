from FileReader import FileReader

fileReader = FileReader()
fileReader.parse("C:\\Users\\esriyag\\PycharmProjects\\scratch\\db\\users")

username = input("Username:")
password = input("Password:")

user = fileReader.get_row(username)
if user is not None:
    if username == user[0] and password == user[1]:
        print("Logged in successfully")
        print("Full name: %s" %user[2])
        print("Phone number: %s" % user[3])
        exit(0)

print("Wrong username or password!!!")
