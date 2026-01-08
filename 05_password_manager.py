master_pwd = input("What is the master password? ")

def view():
    with open('passwords.txt', 'r') as f:  
        for line in f.readlines():
            print(line.rstrip())


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    # w mode: overwrite / r mode: only reading / a mode: creating and write
    with open('passwords.txt', 'a') as f:  # need to close if you write 'file = open('~')' so using with as is better
        f.write(name + "|" + pwd + "\n")


while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit ").lower()
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")