import random
import pymongo

def generateID():
    try:
        # Establishing a connection with the MongoDB server
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["CMS"]
        Customers = db["Customers"]
        
        # Characters used to generate the ID and setting ID length
        characters = "1234567890qwertyuiopasdfghjklzxcvbnm"
        length_id = 5
        
        # Keep generating a unique ID until one is found
        while True:
            # Generating a random ID
            unique_id = "".join(random.choices(characters, k=length_id))
            
            # Check if the ID already exists in the database
            if Customers.count_documents({"_id": unique_id}) == 0:
                return unique_id  # Return the unique ID if not found in database

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
