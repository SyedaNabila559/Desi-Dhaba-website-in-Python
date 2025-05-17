# Class 09 Assignment - May 12

# Ten Dollar ($10) Challenge (3rd Week)

# Create a unique web application by applying OOP principles in python.

# Desi Dhaba 🍽️
Welcome to Desi Dhaba, your ultimate destination for authentic, flavorful, and heartwarming Pakistani food. From mouth-watering Biryani to sizzling Seekh Kebabs, we have it all! 🥘🍛

This application lets users explore the menu, place orders, and enjoy a seamless online food experience. Admin users can manage the menu and remove or add dishes to the offerings.

# Features 🚀
Login / Signup 🔐: Secure user authentication with email and password.

Menu Management 🍴: View the menu and add or remove dishes (Admin only).

Order System 🛒: Browse and add items to the cart.

Checkout ✅: Confirm your order and choose your payment method.

Responsive Design 📱💻: Accessible on both desktop and mobile devices.

Admin Panel ⚙️: Admin users can manage the restaurant's menu.

# Technologies Used 💻
Streamlit: For building interactive web applications with minimal code.

Python OOP: Object-Oriented Programming principles to structure the application and improve maintainability.

Simulated Data: User authentication, menu items, and order management are all simulated with dummy data for demonstration purposes.

# OOP Classes Used in the Application 🧑‍💻
The code utilizes Object-Oriented Programming (OOP) principles to structure and organize the application. Below are the main classes used:

# 1. User Class 👤
Purpose: Represents a user in the application, including login credentials and details.

# Attributes:

username: The user's name.

email: The user's email address.

Methods: No specific methods are implemented, but this class is used for managing user details.

# 2. MenuItem Class 🍽️
Purpose: Represents a menu item in the restaurant's menu.

# Attributes:

name: Name of the dish (e.g., Biryani, Chicken Karahi).

price: Price of the dish.

description: A brief description of the dish (optional).

image_path: Path to the image of the dish (optional).

Methods: This class is primarily used for data storage and doesn't have specific methods.

# 3. Order Class 🛒
Purpose: Manages the user's order, including adding items to the cart and calculating the total price.

# Attributes:

items: A list that holds all the menu items added to the order.

# Methods:

add_item: Adds a MenuItem object to the items list.

total_price: Calculates the total price of all items in the cart.

clear: Clears the order after checkout.

# 4. Restaurant Class 🏪
Purpose: Represents the restaurant, its menu, and its operations (e.g., adding new menu items).

# Attributes:

name: The name of the restaurant.

menu: A list of all MenuItem objects available in the menu.

# Methods:

add_menu_item: Adds a MenuItem to the restaurant's menu.

get_menu: Returns the list of all MenuItem objects in the menu.

# How to Use 📝
Run the App 💻:
To run the application, simply clone the repository and use Streamlit to start the server:


git clone https://github.com/SyedaNabila559/Desi-Dhaba-website-in-Python
cd Desi-Dhaba

streamlit run app.py

# Login or Signup 🔑:
If you are a new user, click "Go to Signup" and create an account. If you already have an account, simply log in using your credentials.

# Browse the Menu 🍲:
After logging in, you'll be able to explore the available dishes. Click on "Add to Cart" to start ordering your favorite food.

# Place an Order 🛍️:
Once you've added items to the cart, go to the "Checkout" page to confirm your order and select your payment method.

# Admin Access 👑:
Admin users can access the Admin Panel to manage the menu, including adding and removing dishes. Admin Login is required for this.

# Important Features for Admin 👨‍🍳
Add new menu items with details (Name, Price, Description, Image).

Remove existing menu items.

Admin panel access is protected by login credentials.

# $10 Challenge! 💸🔥

"I may not be the best at coding, but I’m giving my all and facing every error like a champ! Now, let’s see who wins this battle of bugs and logic! 💻⚡😎

# "Errors are proof that you are trying."😅💻💡

# Happy Coding, and may your errors turn into lessons! 💡✨


