from FileReader import FileReader

fileReader = FileReader()
fileReader.parse("C:\\Users\\esriyag\\PycharmProjects\\scratch\\db\\users")

username = input("Username:")
password = input("Password:")

user = fileReader.get_row(username)
if user is not None:
    print(user[0])
    print(user[1])
    print(user[2])
else:
    print("Wrong username")
