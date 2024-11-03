def validate(choice,givenList):
    try:
        choice = int(choice)
        if choice not in givenList:
            return False
    except Exception as e:
        if choice == "exit":
            exit(0)
        e = "invlaid"
        return e
    return True


def checkChoice(choice,givenList):
    
    if validate(choice,givenList) == True:

        return True
    else:
        return False
    

def connectException():
    return "cannot connect check internet"
