import streamlit as st

# ------------------ OOP Classes ------------------

class User:
    def __init__(self, username, email, role="user"):
        self.username = username
        self.email = email
        self.role = role  # Added role for user or admin

class MenuItem:
    def __init__(self, name, price, description="", image_path=""):
        self.name = name
        self.price = price
        self.description = description
        self.image_path = image_path

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, menu_item):
        self.items.append(menu_item)

    def total_price(self):
        return sum(item.price for item in self.items)

    def clear(self):
        self.items = []

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = []

    def add_menu_item(self, item):
        self.menu.append(item)

    def remove_menu_item(self, index):
        if 0 <= index < len(self.menu):
            del self.menu[index]

    def get_menu(self):
        return self.menu

# ------------------ Setup Data ------------------
restaurant = Restaurant("Desi Dhaba")

items_data = [
    ("Biryani", 250, "Spicy Hyderabadi Biryani", "images/baryani.png"),
    ("Chicken Karahi", 350, "Tender chicken cooked in a spicy karahi", "images/chicken-karahi.png"),
    ("Nihari", 400, "Slow-cooked beef stew with spices", "images/nahari.png"),
    ("Chapli Kebab", 200, "Spicy minced meat kebabs", "images/chapli-kabab.png"),
    ("Seekh Kebab", 250, "Minced meat kebabs grilled to perfection", "images/Seekh-Kebab.png"),
    ("Samosa", 30, "Crispy fried pastry filled with spiced potatoes", "images/samosay.png"),
    ("Pakora", 50, "Fried gram flour fritters with spices", "images/pakory.png"),
    ("Chana Chaat", 100, "Spicy chickpea salad with onions and tomatoes", "images/chana-chat.png"),
    ("Gol Gappa", 80, "Pani puri with spicy tamarind water", "images/golgappy.png"),
    ("Aloo Keema", 220, "Minced meat cooked with potatoes", "images/aloo_qeema.png"),
    ("Korma", 350, "Mutton cooked in a rich creamy gravy", "images/qorma.png"),
    ("Pulao", 180, "Fragrant rice with mixed vegetables", "images/beaf-palao.png"),
    ("Raita", 50, "Cool yogurt-based side dish", "images/raita.png"),
    ("Tandoori Roti", 20, "Traditional tandoor-baked flatbread", "images/tandori roti.png"),
    ("Naan", 25, "Soft, fluffy traditional bread", "images/naan.png"),
    ("Butter Chicken", 280, "Chicken cooked in a creamy tomato-based gravy", "images/butter-chicken.png"),
    ("Saag", 180, "Spinach and mustard leaves cooked with spices", "images/saag.png"),
    ("Makki di Roti", 40, "Corn flatbread served with saag", "images/makki-ki-roti.png"),
    ("Paya", 400, "Slow-cooked goat trotters in a rich spicy gravy", "images/paya.png"),
    ("Daal Tarka", 150, "Spicy lentil curry with tempering", "images/dal-tarka.png"),
    ("Kachori", 60, "Deep-fried pastry filled with spiced lentils", "images/kachuri.png"),
    ("Lassi", 90, "Traditional yogurt drink", "images/lassi.png"),
    ("Zarda", 120, "Sweet rice pudding made with saffron", "images/zarda.png"),
    ("Gulab Jamun", 100, "Fried dough balls soaked in sugar syrup", "images/golab-jalum.png"),
    ("Kheer", 120, "Rice pudding made with milk and cardamom", "images/kheer.png"),
    ("Halwa", 80, "Carrot or semolina-based dessert", "images/halwa.png"),
    ("Fried Fish", 250, "Spicy battered fish fillets", "images/fried-fish.png"),
    ("Roghni Naan", 30, "Soft naan with sesame seeds", "images/roghni-naan.png"),
    ("Bashmati Rice", 100, "Fragrant long-grain rice", "images/banaspati-rice.png"),
    ("Chicken Shawarma", 220, "Grilled chicken wrapped in pita bread", "images/shawarma.png"),
    ("Haleem", 300, "A slow-cooked stew with wheat, meat, and spices", "images/haleem.png"),
    ("Dahi Bhalla", 70, "Soft lentil dumplings soaked in yogurt", "images/dahi-bally.png"),
    ("BBQ Platter", 550, "Assorted grilled kebabs, chicken tikka, and more served with naan", "images/bbq-platter.png"),
    ("Pasta", 220, "Creamy white sauce pasta with vegetables", "images/pasta.png"),
    ("Desi Burger", 150, "Spicy burger with chicken patty", "images/desi-burger.png"),
    ("Vegetable Wrap", 120, "Healthy wrap with mixed veggies and sauces", "images/vegetable-warp.png"),
    ("French Fries", 100, "Crispy golden fries", "images/french-fries.png"),
    ("Pizza", 300, "Veg pizza with loads of cheese", "images/pizza.png"),
    ("Fried Rice", 180, "Vegetable fried rice with soy sauce", "images/fried-rice.png"),
    ("Chicken Wings", 250, "Spicy grilled chicken wings", "images/chicken-wings.png"),
]

for name, price, desc, img in items_data:
    restaurant.add_menu_item(MenuItem(name, price, desc, img))

# ------------------ Session State ------------------
if "order" not in st.session_state:
    st.session_state.order = Order()
if "page" not in st.session_state:
    st.session_state.page = "Login"
if "user" not in st.session_state:
    st.session_state.user = None
if "users_db" not in st.session_state:
    st.session_state.users_db = {}  # Simulated DB

# ------------------ Navigation ------------------
def show_sidebar():
    st.sidebar.title("🍽️ Navigation")
    if st.session_state.user:
        pages = ["Home", "Order", "Checkout", "About", "Contact", "Logout"]
        if st.session_state.user.role == "admin":
            pages.insert(-1, "Admin Panel")  # Admin Panel added
        page = st.sidebar.radio("Go to", pages, index=pages.index(st.session_state.page))
        st.session_state.page = page
    else:
        st.sidebar.info("Please log in to access the menu.")

# ------------------ Auth Pages ------------------
def login_page():
    st.title("🔐 Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if email in st.session_state.users_db and st.session_state.users_db[email]["password"] == password:
            user_data = st.session_state.users_db[email]
            st.session_state.user = User(user_data["username"], email, user_data["role"])
            st.success(f"Welcome back, {st.session_state.user.username}!")
            st.session_state.page = "Home"
            st.rerun()
        else:
            st.error("Invalid credentials.")

    st.markdown("Don't have an account?")
    if st.button("Go to Signup"):
        st.session_state.page = "Signup"
        st.rerun()

def signup_page():
    st.title("📝 Signup")
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if email == "admin@desidhaba.pk":
        role = "admin"  # Default admin
    else:
        role = "user"  # Default role for other users

    if st.button("Create Account"):
        if email in st.session_state.users_db:
            st.warning("User already exists.")
        else:
            st.session_state.users_db[email] = {"username": username, "password": password, "role": role}
            st.success("Account created! Please log in.")
            st.session_state.page = "Login"
            st.rerun()

# ------------------ Admin Panel ------------------
def admin_panel():
    st.title("🛠️ Admin Panel")

    st.subheader("➕ Add New Menu Item")
    name = st.text_input("Dish Name")
    price = st.number_input("Price", min_value=0)
    description = st.text_area("Description")
    image_path = st.text_input("Image Path (e.g. images/dish.png)")

    if st.button("Add Dish"):
        restaurant.add_menu_item(MenuItem(name, price, description, image_path))
        st.success(f"{name} added to menu!")

    st.subheader("🗑️ Remove Existing Menu Items")
    for i, item in enumerate(restaurant.get_menu()):
        cols = st.columns([3, 1])
        cols[0].markdown(f"**{item.name}** - ₹{item.price}")
        if cols[1].button("❌ Remove", key=f"remove_{i}"):
            restaurant.remove_menu_item(i)
            st.warning(f"{item.name} removed.")
            st.rerun()

# ------------------ Main Pages ------------------
def home_page():
    st.image("images/logo.png", width=150)

    st.markdown("""
        <div style='text-align: center; padding: 2rem;'>
            <h1 style='color: #FF4B4B;'>🍲 Welcome to Desi Dhaba! </h1>
            <h3>Your favorite stop for delicious desi food 🍛</h3>
            <p>Scroll down to explore our mouth-watering menu!</p>
        </div>
    """, unsafe_allow_html=True)

    st.subheader("📜 Explore Our Menu")
    for item in restaurant.get_menu():
        with st.container():
            cols = st.columns([1, 3])
            with cols[0]:
                st.image(item.image_path, width=120)
            with cols[1]:
                st.markdown(f"### {item.name} - ₹{item.price}")
                st.markdown(f"*{item.description}*")
                if st.button("🛒 Add to Cart", key=f"add_to_cart_{item.name}"):
                    st.session_state.order.add_item(item)
                    st.success(f"{item.name} added to cart!")

def order_page():
    st.title("🛒 Your Cart")
    if st.session_state.order.items:
        for i, item in enumerate(st.session_state.order.items, 1):
            st.markdown(f"{i}. {item.name} - ₹{item.price}")
        st.markdown(f"### Total: ₹{st.session_state.order.total_price()}")
        if st.button("Go to Checkout"):
            st.session_state.page = "Checkout"
            st.rerun()
    else:
        st.info("Your cart is empty. Go to Home and add items.")

def checkout_page():
    st.title("✅ Checkout")
    if st.session_state.order.items:
        st.success("Thanks for your order! 🍽️")
        st.write("You ordered:")
        for item in st.session_state.order.items:
            st.markdown(f"- {item.name} - ₹{item.price}")
        st.markdown(f"### Total Bill: ₹{st.session_state.order.total_price()}")

        payment_method = st.selectbox("Choose Payment Method", ["Cash on Delivery", "Simulated Card", "UPI"])
        if st.button("Confirm Payment"):
            st.balloons()
            st.success("🎉 Order placed successfully!")
            st.session_state.order.clear()
    else:
        st.warning("Your cart is empty.")

def about_page():
    st.title("📖 About Us")
    st.markdown("""
    Welcome to Desi Dhaba, your ultimate destination for authentic, heartwarming, and flavorful Pakistani food!

    Our menu features a wide range of mouthwatering dishes, from rich, aromatic biryanis to sizzling kebabs, all cooked using recipes passed down through generations.

    Every dish is prepared with love and care, using fresh, locally sourced ingredients.

    It’s not just a meal; it's a celebration of the true taste of Pakistan!
    """)

def contact_page():
    st.title("📞 Contact Us")
    st.markdown("""
    - 📱 Phone: +92-33345324  
    - 📧 Email: DesiDhaba@gmail.com  
    - 📍 Location: Karachi, Pakistan  
    """)

# ------------------ Routing ------------------
if st.session_state.page == "Login":
    login_page()
elif st.session_state.page == "Signup":
    signup_page()
else:
    show_sidebar()
    if st.session_state.page == "Home":
        home_page()
    elif st.session_state.page == "Order":
        order_page()
    elif st.session_state.page == "Checkout":
        checkout_page()
    elif st.session_state.page == "About":
        about_page()
    elif st.session_state.page == "Contact":
        contact_page()
    elif st.session_state.page == "Admin Panel":
        if st.session_state.user.role == "admin":
            admin_panel()
        else:
            st.error("Access Denied: You are not an admin.")
    elif st.session_state.page == "Logout":
        st.session_state.user = None
        st.session_state.page = "Login"
        st.success("Logged out successfully.")
        st.rerun()



