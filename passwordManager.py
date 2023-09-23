from cryptography.fernet import Fernet

''' 
def writeKey():
    key = Fernet.generate_key()
    with open('key.key', "wb") as keyFile:
        keyFile.write(key)        
'''

def loadKey():
    with open('key.key', "rb") as keyFile:
        key = keyFile.read()
        return key

key = loadKey()
fer = Fernet(key) #this will be used to encrypt the password when adding in the file, it is a module initializer

def add(username, password):
    encrypted_password = fer.encrypt(password.encode())
    with open('passwords.txt', 'a') as file:
        file.write(username + " | " + encrypted_password.decode() + "\n")


def view():
    with open('passwords.txt', 'r') as file:
        for line in file.readlines():
            data = line.rstrip()  # Data to break
            username, encrypted_password = data.split("|")
            password = fer.decrypt(encrypted_password.encode()).decode()
            print(f"Username = {username} | Password = {password}")


 

def main():
    masterPassword = input("Enter the master password: ") #have to integrate this with the key
    
    while True:
        mode = input("Enter \"add\" to add a password\n"
                    "Enter \"view\" to view a password\n"
                    "Enter \"q\" to quit\n"
                    "Enter a valid option: ").lower()
        
        if mode == "q":
            quit()

        if mode == "add":
            username = input("Enter a username to add: ")
            password = input(f"Enter the password of {username}: ")
            add(username, password)
        elif mode == "view":
            view()

        else:
            print("Enter a valid option: ")
            continue
        
main()


    
    

