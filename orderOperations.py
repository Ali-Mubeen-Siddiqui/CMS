



def frameOrders(orderTemplate,price):
    count = 1
    mapping = {}
    if len(orderTemplate) == 0:
        print("No orders registered yet. ")
        
    for order,quan in orderTemplate.items():
        print("order  -> quantity")
        
        print(f"{count})  {order}    ->      {quan}")
        count += 1
        mapping[count] = order
    
        if len(orderTemplate) == count:
            print("-------------------")
            print(f"Totsal orders: {count}")
            print(f"Total Price : {price}")

    return mapping


    