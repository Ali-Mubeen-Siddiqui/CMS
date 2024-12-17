import pymongo
from utilities import checkChoice,connectException

# imports
# admin class


class Admin:
    def __init__(self):
        try:
            self.client = pymongo.MongoClient("mongodb://localhost:27017/")
            self.db = self.client["CMS"]
            self.admin = self.db["admin"]
            self.condition = "run"
        except Exception as e:
            e = connectException()
            print(e)
    def isAdmin(self,username,password):
        try:
            if self.admin.find_one({"userName":username,"password":password}):
                self.adminData = self.admin.find_one({"userName":username,"password":password})
                return True
            else:
                return False
        except Exception as e:
            e = connectException()
            print(e)

    def getPost(self):
        try:
            self.post = self.adminData["post"]
            return self.post
        except Exception as e:
            e = connectException()
            print(e)

    

    def permissions(self,post):
        try:
            self.postInfo = self.db["PostData"]
            self.postInfo = self.postInfo.find_one({"_id":post})
            return self.postInfo["permit"]
        except Exception as e:
            e = connectException()
            print(e)

    def fetchData(self):
        try:
            self.userName = self.adminData["userName"]
            self.post = self.getPost()
            self.Id = self.adminData["_id"]
        except Exception as e:
            e = connectException()
            print(e)


    def Page(self):
        self.fetchData()
        print(f"""____________________welcome {self.userName}____________________\n
                    Post: {self.post}
                    Id: {self.Id}\n
___________________________________________________\n""")
        self.showOpt()


    def showOpt(self):
        print("""1)View Options
2)Logout[Always logout before closing the program]""")
        self.processChoice()

    def choice(self):
        self.ch = input("Enter your choice: ")
        if checkChoice(self.ch,[1,2]):
            return self.ch.strip()
        else:
            print("Invalid choice")
            
        
        
    def processChoice(self):
        self.reChoice = self.choice()
        if self.reChoice == "1":
            self.showControls()
        elif self.reChoice == "2":
            self.logout()


    def logout(self):
        islogout = input("Are you sure you want to logout (yes/no): ")
        if islogout.strip().lower() == "yes":
            self.condition = "break"
        else:
            self.Page()


    def showControls(self):
        print("""1)View Customers
2)View Orders
3)View Items
4)View Admins
5)Add Admin""")
        self.askControl()

    def askControl(self):
        self.cont = input("enter your choice: ")
        if checkChoice(self.cont,[1,2,3,4,5,6]):
            self.redirectControl(self.cont.strip())

        else:
            print("invalid input")

    def redirectControl(self,controlNumber):
        self.cont = controlNumber
        if self.cont == "1":
            print("loading customers")
            self.viewCustomers()
        elif self.cont == "2":
            self.viewOrders()
        elif self.cont == "3":
            self.viewItems()
        elif self.cont == "4":
            self.viewPost()
        elif self.cont == "5":
            self.addNewPost()
        


    def viewCustomers(self):
        self.permit = self.permissions(self.post)
        if self.permit == "_all" or "viewCustomers" in self.permit:
            try:
                self.customer = self.db["Customers"]
                self.customerData = self.customer.find()
                self.frameCustomerData()
                justchk = input("do you want to view a specific customer by id (yes/no): ")
                if justchk.strip().lower() == "yes":
                    id = input("enter the id: ")
                    # User has requested to view a specific customer
                    self.getSpecificCustomerById(id)
            except Exception as e:
                e = connectException()
                print(e)
        else:
            print("you don't have permission to view customers")

    def viewOrders(self):
       self.permit = self.permissions(self.post)
       if self.permit == "_all" or "viewOrders" in self.permit:
           print("loading orders")
           self.customer = self.db["Customers"]
           self.customerData = self.customer.find()
           self.frameOrder()

           justchk = input("do you want to view a specific customer by dish (yes/no): ")
           if justchk.strip().lower() == "yes":
            dish = input("enter the dish: ")
            # User has requested to view a specific customer
            self.getSpecificCustomerByDish(dish)

       else:
           print("you don't have permission to view orders")

    def viewItems(self):
        print("loading items")
        self.item = self.db["Menu"]
        for item in self.item.find():
            print(f"dish  : {item.get('_id')}   ->   price : {item.get('ratePer')}")

        self.justchk = input("do you want to add a new item to the menu (yes/no): ")
        if self.justchk.strip().lower() == "yes":
            self.addItemtomenu()

        self.justchk = input("do you want to delete an item from the menu (yes/no): ")
        if self.justchk.strip().lower() == "yes":
            self.deleteItemFromMenu()

    def addItemtomenu(self):
        self.permit = self.permissions(self.post)
        if self.permit == "_all" or "addItemtomenu" in self.permit: 
            self.itemName = input("enter the dish name: ")
            self.itemPrice = input("enter the rate in rate/per format: ")
            self.itemRate = input("enter the rate : ")
            try:
                self.itemRate = int(self.itemRate)
            except Exception as e:
                print("invalid input")
                

            try:    
                self.item = self.db["Menu"]
                self.item.insert_one({"_id":self.itemName,"ratePer":self.itemPrice,"rate":self.itemRate}) 
                print("item added successfully")
            except Exception as e:
                e = connectException()
                print(e)
        else:
            print("you don't have permission to add items to the menu")

    def deleteItemFromMenu(self):
        self.permit = self.permissions(self.post)
        if self.permit == "_all" or "deleteItemtomenu" in self.permit: 
            self.itemName = input("enter the dish name: ")
            try:
                self.item = self.db["Menu"]
                self.item.delete_one({"_id": self.itemName})
                print("item successfully deleted.")

            except Exception as e:
                e = connectException()
                print(e)
        else:
            print("you do not have the permit.")

        
     

        
    def viewPost(self):
       
        self.permit = self.permissions(self.post)
        if self.permit == "_all":
            try:
                adminAvail = self.admin.find({})
                for member in adminAvail:
                    print("__________________________________")
                    print(f"{member.get("userName")}      -->    {member.get("post")}  -->  {member.get("_id")}")

            except Exception as e:
                e  = connectException()
                print(e)

        else:
            print("you do not have the permit.")



    def addNewPost(self):
        
        self.permit = self.permissions(self.post)
        if self.permit == "_all":
            self.temp = {}
            try:
                self.inName = input("enter name of the employee : ").lower()
                self.inPost = input(f"enter post of {self.inName}  : ").strip().lower()
                self.id_ = input("enter an Id for the employee : ")
                self.passkey = input("enter a strong password :")

                self.temp = {
                    "_id": self.id_,
                    "userName": self.inName,
                    "password": self.passkey,
                    "post": self.inPost
                }
                self.admin.insert_one(self.temp)
                print(f"successfully added {self.isName} to admins")

            except Exception as e:
                e = connectException()
                print(e)

   


    def frameCustomerData(self):
        
        self.customData = list(self.customerData)  # Convert cursor to list
        if not self.customData:
            print("No customers found.")
            return

        for customer in self.customData:
            print("\n")
            print("===========================================================")
            print(f"Customer ID: {customer.get('_id', 'N/A')}")
            print(f"Table Number: {customer.get('tableNumber', 'N/A')}")
            print(f"Total Amount: ${customer.get('totalAmount', 0):.2f}")
            print(f"Total Orders: {customer.get('totalOrders', 0)}")
            print("\nOrders:")
            orders = customer.get('orders', {})
            if orders:
                for order, qua in orders.items():
                    print(f"  - {order}: {qua}")
            else:
                print("  No orders")
            print("\n")
        
        print(f"Total number of customers: {len(self.customData)}")

    def getSpecificCustomerById(self, id):
        try:
            self.requiredData = self.customer.find_one({"_id": id})
          
            if self.requiredData is not None:
                
                print("\nCustomer Details:")
                print(f"Table Number: {self.requiredData.get('tableNumber', 'N/A')}")
                print(f"Total Amount: ${self.requiredData.get('totalAmount', 0):.2f}")
                print(f"Total Orders: {self.requiredData.get('totalOrders', 0)}")
                print("\nOrders:")
                orders = self.requiredData.get('orders', {})
                if orders:
                    for order, quantity in orders.items():
                        print(f"  - {order}: {quantity}")
                else:
                    print("  No orders")
            else:
                print(f"Customer with ID '{id}' not found")
        except Exception as e:
            e = connectException()
            print(e)
    def frameOrder(self):
   
        for customerDO in self.customerData:
            print("\n________________________________________________________")
            print(f"Table Number: {customerDO.get('tableNumber', 'N/A')}")
            print("Orders:")
            orders = customerDO.get('orders', {})
            if orders:
                for order, quantity in orders.items():
                    print(f"  - {order}: {quantity}")
            else:
                print("  No orders")
            print(f"Total Amount: ${customerDO.get('totalAmount', 0):.2f}")
            print(f"Total Orders: {customerDO.get('totalOrders', 0)}")




    def getSpecificCustomerByDish(self, dish):
        print("loading customers who ordered the dish")
        try:
            # Find all customers who have ordered the specified dish
            
            customers_with_dish = self.customer.find({"orders." + dish: {"$exists": True}})
            
            
            customers_with_dish_list = list(customers_with_dish)
            if customers_with_dish_list:
                print(f"\nCustomers who ordered {dish}:")
                for customer in customers_with_dish_list:
                    print("\n________________________________________________________")
                    print(f"Customer ID: {customer['_id']}")
                    print(f"Table Number: {customer.get('tableNumber', 'N/A')}")
                    print(f"Quantity ordered: {customer['orders'].get(dish, 0)}")
                    print(f"Total Amount: ${customer.get('totalAmount', 0):.2f}")
                    print(f"Total Orders: {customer.get('totalOrders', 0)}")
                    print("\nAll Orders:")
                    orders = customer.get('orders', {})
                    for order, quantity in orders.items():
                        print(f"  - {order}: {quantity}")
            else:
                print(f"No customers found who ordered '{dish}'")
        except Exception as e:
            e = connectException()
            print(e)


# this file is for admin panel



