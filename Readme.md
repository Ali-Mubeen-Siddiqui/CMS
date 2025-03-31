# Project Title: CMS (Content Management System)

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [MongoDB Database Structure](#mongodb-database-structure)
- [Contributing](#contributing)
- [License](#license)

## Description
This project is a **Content Management System (CMS)** designed specifically for managing customer orders and administrative functionalities in a restaurant setting. The CMS provides a user-friendly interface for both admins and customers, allowing for efficient management of menu items, customer orders, and overall data handling.

### Purpose
The primary goal of this CMS is to streamline the ordering process in restaurants, enabling admins to manage menu items and view customer orders while providing customers with an easy way to place orders and view available dishes.

## Features
- **Admin Functionalities**:
  - Manage menu items (add, delete, and view).
  - View customer orders and details.
  - Add and manage admin users.
  
- **Customer Interface**:
  - Place orders for menu items.
  - View the menu and item details.
  - Cancel orders if needed.
  
- **Data Management**:
  - MongoDB integration for efficient data storage and retrieval.
  - Real-time updates to customer orders and menu items.

## Installation
To set up the CMS on your local machine, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install dependencies**:
   Ensure you have Python and pip installed. Then run:
   ```bash
   pip install pymongo
   ```

3. **Set up MongoDB**:
   - Ensure you have MongoDB installed and running on your local machine.
   - The default connection string used in the code is `mongodb://localhost:27017/`. Make sure this is correctly configured in your environment.

## Usage
1. **Run the Admin Panel**:
   To start the admin functionalities, execute:
   ```bash
   python Admin.py
   ```
   - Follow the prompts to manage menu items and view customer orders.

2. **Run the Customer Interface**:
   To start the customer functionalities, execute:
   ```bash
   python CustomerPage.py
   ```
   - Customers can place orders, view the menu, and manage their orders through this interface.

3. **Follow the prompts** in the console to navigate through the options. The system will guide you through various functionalities based on your role (admin or customer).

## MongoDB Database Structure
The MongoDB database for this project is structured as follows:

### Database: `CMS`
- **Collection: `admin`**
  - **Documents contain**:
    - `_id`: Unique identifier for the admin (string)
    - `userName`: Admin's username (string)
    - `password`: Admin's password (string, should be hashed for security)
    - `post`: Admin's role (string, e.g., "superadmin", "manager")

- **Collection: `Customers`**
  - **Documents contain**:
    - `_id`: Unique identifier for the customer (string)
    - `paymentMethod`: Method of payment (string, e.g., "credit card", "cash")
    - `orders`: A dictionary of ordered items (key: dish name, value: quantity)
    - `totalOrders`: Total number of orders placed (integer)
    - `tableNumber`: Table number associated with the customer (integer)
    - `totalAmount`: Total amount for the orders (float)

- **Collection: `Menu`**
  - **Documents contain**:
    - `_id`: Unique identifier for the menu item (string)
    - `ratePer`: Rate per item (string, e.g., "10.99")
    - `rate`: Total rate for the item (integer, e.g., 10)

### Example Document Structure
**Admin Document**:
```json
{
  "_id": "admin123",
  "userName": "adminUser",
  "password": "hashedPassword",
  "post": "superadmin"
}
```

**Customer Document**:
```json
{
  "_id": "customer456",
  "paymentMethod": "credit card",
  "orders": {
    "Pasta": 2,
    "Salad": 1
  },
  "totalOrders": 3,
  "tableNumber": 5,
  "totalAmount": 35.97
}
```

**Menu Document**:
```json
{
  "_id": "Pasta",
  "ratePer": "10.99",
  "rate": 10
}
```

## Contributing
Contributions are welcome! If you would like to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

Feel free to open an issue for any suggestions or improvements.

## License
This project is currently unlicensed.

---

Thank you for using the CMS! We hope it enhances your restaurant management experience.
