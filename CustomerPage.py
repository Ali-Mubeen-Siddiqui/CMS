import pymongo
from randID import generateID
from quotes import *
from utilities import checkChoice
from orderOperations import frameOrders
# imports are till here only


class Customer:
    def __init__(self):
        self.ID = generateID()
        self.paymentMethod = None
        self.orders = None
        self.tableNumber = None
        self.totalAmount = 0
        self.totalOrd = 0
        self.template = {
            "_id": self.ID,
            "paymentMethod": self.paymentMethod,
            "orders": self.orders,
            "totalOrders": self.totalOrd,
            "tableNumber": self.tableNumber,
            "totalAmount": self.totalAmount,
        }
        self.orderTemplate = {}

        # Connect to the local MongoDB server with error handling
        try:
            self.client = pymongo.MongoClient("mongodb://localhost:27017/")
            self.db = self.client["CMS"]
            mymenu = self.db["Menu"]
        except pymongo.errors.ConnectionFailure as e:
            print("Could not connect to MongoDB: ", e)

    def ask(self):
        print(f"Your ID is : {self.ID}")
        print(interfaceCustomer)
        self.choice = input("Please enter your choice: ")
        
        if checkChoice(self.choice, [1, 2, 3, 4, 5]):
            if self.choice == "1":
                print(orderView)
                ch = input("Please enter your choice: ")
                
                if checkChoice(ch, [1, 2]):
                    if ch.strip() == "1":
                        myMenu = self.db["Menu"]
                        menuItems = myMenu.find({})
                        print("        Our Menu     \n")
                        
                        for item in menuItems:
                            print(f"    {item['_id']}   |        {item['rate']}")
                    elif ch.strip() == "2":
                        self.orderItem()
            elif self.choice == "2":
                myMenu = self.db["Menu"]
                menuItems = myMenu.find({})
                print("        Our Menu     \n")
                
                for item in menuItems:
                    print(f"    {item['_id']}   |        {item['rate']}")
            elif self.choice == "3":
                frameOrders(self.orderTemplate,self.totalAmount)


              
            elif self.choice == "4":
                orderMapping = frameOrders(self.orderTemplate,self.totalAmount)
                lsDir = []
                for num in range(self.totalOrd + 1):
                    lsDir.append(num)

                self.selectOrder = input("Please enter the order Number: ")
                if checkChoice(self.selectOrder,lsDir):
                    self.orderTemplate.pop(self.order)
                    self.fetchOrder = myMenu.find_one({"_id": orderMapping[self.selectOrder]})
                    for ord in self.fetchOrder:
                        self.totalAmount -= ord["rate"] * ord["quantity"]
                        self.totalOrd -= 1
                        print("Order cancelled successfully.")
                   
                



                pass  
            elif self.choice == "5":
                islogout = input("Are you sure you want to logout (yes/no): ")
                if islogout.strip().lower() == "yes":
                    return "break"
                
    def orderItem(self):
        self.order = input("Please enter a dish name: ").strip().lower()
        mymenu = self.db["Menu"]
        self.item = mymenu.find_one({"_id": self.order})
        
        if not self.item:
            print("Sorry, this dish is not available.")
            return
        
        self.itemRate = self.item["rate"]
        self.quantity = int(input(f"Please enter quantity (Rate: {self.item['ratePer']}): "))
        
        if self.tableNumber is None:
            try:
                self.tableNumber = int(input("Please enter the table number: "))
            except ValueError:
                print("Please enter a valid number")
                return
            
        if self.order not in self.orderTemplate:
            self.orderTemplate[self.order] = self.quantity
        else:
            self.orderTemplate[self.order] += self.quantity
        
        self.totalAmount += self.itemRate * self.quantity
        self.template.update({
            "tableNumber": self.tableNumber,
            "orders": self.orderTemplate,
            "totalAmount": self.totalAmount,
            "totalOrders":self.totalOrd+1
        })
        
        customerList = self.db["Customers"]
        similarCustomer = customerList.find_one({"_id": self.ID})
        if similarCustomer is None:
            customerList.insert_one(self.template)
            print("Your order has been placed successfully.")
        else:
            customerList.update_one(
                {"_id": self.ID},
                {"$set": self.template}
            )
            print("Order added successfully.")



            # complete page
