with open("test.txt","w") as file:
    file.write("hello world. ")





with open("test.txt","a") as file:
    file.write("i am nusaybah")


with open("test.txt","r") as file:
    print(file.read())