from quotes import welcome
from utilities import validate,checkChoice
from CustomerPage import Customer
from Admin import Admin


def createadmin():
    user = Admin()
    userName = input("Enter username: ")
    password = input("Enter password: ")
    if user.isAdmin(userName.strip().lower(),password):
        runAdmin = True
        while runAdmin:
            user.Page()
            if user.condition == "break":
                break
            
            
    else:
        print("Invalid credentials")



def createCustomer():
    runcust = True
    user = Customer()
    while runcust:
        isrunning = user.ask()
        if isrunning == "break":
           break

def main():
    run = True
    while run:
       print(welcome)
       choice = input("Choose an option (1/2): ")
       if checkChoice(choice,[1,2]):
           if choice.strip() == "1":
               createadmin()
               
           elif choice.strip() == "2":
               createCustomer()
                
                

               

if __name__ == "__main__":
    main()