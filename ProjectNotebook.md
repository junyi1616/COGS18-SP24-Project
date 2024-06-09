# Welcome to the Chinese Restaurant!

This project is a Python-based restaurant ordering chatbot designed to enhance customer service efficiency in a restaurant setting. The chatbot interacts with customers, presenting them with a menu of Chinese dishes, taking their orders, calculating the total price, and determining the change to be given back after payment.

**Components:**
1. Menu Information File (menu.py):

- Contains a dictionary of Chinese dishes and their respective prices.
- Provides a function to retrieve the menu data.
- We put the menu information in menu.py, so that it is more convenient for restaurant managers to update the new menu information in the future.

2. Main Program (chatbot.py):

- Handles the main logic for the chatbot.
- Displays the menu to customers.
- Takes customer orders and records the quantity of each dish.
- Calculates the total cost of the order.
- Processes payment and calculates the change to be returned.

3. Functionality:

- Menu Presentation: The chatbot lists available dishes along with their prices to the customer.
- Order Taking: Customers can input the names and quantities of the dishes they want to order. The chatbot handles multiple orders and quantities.
- Total Calculation: The chatbot calculates the total cost based on the customer’s order.
- Payment Processing: After receiving the payment amount from the customer, the chatbot calculates and displays the change.

**Purpose:**
- The primary goal of this project is to create a user-friendly and efficient ordering system for a Chinese restaurant. By automating the order-taking process, the chatbot reduces the workload on restaurant staff and minimizes errors in order processing and payment handling.

- This project is structured to allow easy modification and extension, such as adding new dishes to the menu or enhancing the interaction capabilities of the chatbot. It serves as a practical example of using Python for developing interactive command-line applications.

## Project Code

If it makes sense for your project, you can have code and outputs here in the notebook as well.


```python
from chatbot import start_chatbot
```


```python
#Run this cell to order the food.
start_chatbot()
```

    Menu:
    Sweet and Sour Pork: $12.50
    Kung Pao Chicken: $10.00
    Ma Po Tofu: $8.50
    Spring Rolls: $4.00
    Dumplings: $6.00
    Fried Rice: $7.50
    Hot and Sour Soup: $5.00
    Wonton Soup: $6.50
    Peking Duck: $25.00
    
    
    Welcome to our restaurant! Please place your order.
    
    Enter the name of the dish you want to order (or type 'done' to finish): Peking Duck
    How many of Peking Duck would you like? 1
    Enter the name of the dish you want to order (or type 'done' to finish): Dumplings
    How many of Dumplings would you like? 6
    Enter the name of the dish you want to order (or type 'done' to finish): Fried Rice
    How many of Fried Rice would you like? 3
    Enter the name of the dish you want to order (or type 'done' to finish): done
    
    Your total is: $83.50
    Enter the amount you are paying: 100
    Thank you for your payment. Your change is: $16.50


#### Extra Credit (*optional*)

I have no Python background and have never coded before. I think my project went above and beyond the requirements and I challenged myself. Despite being new to programming, I successfully implemented a chatbot for ordering food using Python. I went beyond the basic requirements by not only creating the chatbot but also writing more functions than what the project required. Throughout the project, I challenged myself to learn Python syntax, programming concepts, and testing it, which all significantly expanded my understanding of programming fundamentals.
