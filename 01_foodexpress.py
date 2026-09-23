#================================================================================
#          FOODEXPRESS: FOOD DELIVERY ANALYTICS TOOLKIT (SESSIONS 1 - 7)
#================================================================================

# PHASE 1 - CAPTURE THE RAW INPUTS

from functools import reduce
import functools
import pandas as pd

print("\nPHASE 1 - CAPTURE RAW INPUTS")

# Restaurant details
restaurant_name = input("Enter restaurant name: ")
city = input("Enter city: ")
owner_age = int(input("Enter owner age: "))

# Order details
item_price = float(input("\nEnter item price: "))
quantity = int(input("Enter quantity: "))
gst_percent = float(input("Enter GST percentage: "))

# Calculate subtotal
subtotal = item_price * quantity

# Calculate GST
gst_amount = (subtotal * gst_percent) / 100.0

# Calculate final bill
final_bill = subtotal + gst_amount

# Check free delivery
free_delivery = final_bill > 199.0

# Add packaging fee using +=
packaging_fee = 20.0
final_bill += packaging_fee

print(f"Restaurant Name: {restaurant_name} | City: {city} | Owner Age: {owner_age}")
print(f"Item Price: Rs. {item_price} | Quantity: {quantity}")
print(f"Subtotal: Rs. {subtotal:.2f} | "f"GST ({gst_percent}%): Rs. {gst_amount:.2f} | "f"Packaging Fee: Rs. {packaging_fee}")
print(f"Phase 1 Final Bill: Rs. {final_bill:.2f}")
print(f"Qualifies for Free Delivery (Bill > Rs. 199)? "f"{free_delivery}")

# PHASE 2 - TURN SINGLE VALUES INTO A SMALL DATASET

print("\nPHASE 2 - LOOPS, CONDITIONS AND LISTS")

# Delivery fee rule
distance = float(input("\nEnter delivery distance in km: "))

if distance < 2.0:
    delivery_fee = 0
elif distance <= 5:
    delivery_fee = 15.0
else:
    delivery_fee = 30.0

total_with_delivery = final_bill + delivery_fee
print(f"Delivery Distance: {distance} km -> Delivery Fee: Rs. {delivery_fee}")
print(f"Total Order Cost with Delivery Fee: Rs. {total_with_delivery:.2f}")

menu_items = ["Biryani", "Paneer Tikka", "Butter Naan", "Lassi", "Gulab Jamun"]
menu_prices = [320, 240, 50, 80, 100]

print("\n--- FoodExpress Menu Display ---")
for i in range(len(menu_items)):
    print(i + 1, ".", menu_items[i], "- Rs.", menu_prices[i])

# While loop for adding another item
print("\nAdding menu items:")

add_item = "yes"

while add_item.lower() == "yes":

    new_item = input("Enter item name: ")
    new_price = float(input("Enter item price: "))

    menu_items.append(new_item)
    menu_prices.append(new_price)

    add_item = input("Add another item? (yes/no): ")

#List Comprehension & Filtering
order_amounts = [
    180, 450, 320, 150, 600,
    290, 850, 410, 220, 350,
    199, 540, 720, 160, 480,
    310, 620, 270, 510, 390]

print("\n20 Order Amounts:")
print(order_amounts)

orders_above_300 = [amount for amount in order_amounts if amount > 300]

print("\nOrders above Rs.300:")
print(orders_above_300)

#Processing Order
print("\nProcessing Order IDs:")

processed_orders = []

for order_id in range(1, 21):
    if order_id % 5 == 0:
            print("Order", order_id, "is cancelled.")
            continue
    if order_id == 18:
        print("Reached Order ID 18. Stop processing.")
        break

    amount = order_amounts[order_id - 1]
    processed_orders.append((order_id, amount))
    print(f"  [Order #{order_id:02d}] Processed successfully | Amount: Rs. {amount}")

print(f"Active Working Orders Dataset Count: {len(processed_orders)} orders.")

# PHASE 3 - STRUCTURE THE DATASET

# Demonstrate id()

var_a = restaurant_name
var_b = restaurant_name

print("\nBefore Reassignment")
print(f"Memory Address of var_a: {id(var_a)}")
print(f"Memory Address of var_b: {id(var_b)}")
print(f"var_a and var_b share the exact same object? {id(var_a) == id(var_b)}")

# Reassign var_a
var_a = "Biryani House"
print(f"\nAfter reassigning var_a to '{var_a}':")
print(f"New Memory Address of var_a: {id(var_a)}")
print(f"Memory Address of var_b: {id(var_b)}")

# Before Reassignment: Both variables point to the same string object initially.After reassignment, var_a points to a different object.

# Customer name - String
customer_name = "Karsha"

# Loyalty points - Number
loyalty_points = 100

# Past order IDs - List
past_order_ids = [1, 2, 3, 4, 5]

# Fixed delivery coordinates - Tuple
delivery_coordinates = (11.0168,76.9558)

# Dictionary: order_id,order_amount556+
orders_dict = {}

for i in range(len(order_amounts)):
    orders_dict[i + 1] = order_amounts[i]

# Unique restaurants - Set
unique_restaurants = {"HMR","A2B","Anjappar","Dominos"}

print("\n--- Structured Customer Data ---")
print(f"Customer Name (str)         : {customer_name}")
print(f"Loyalty Points (int)        : {loyalty_points}")
print(f"Past Order IDs (list)       : {past_order_ids[:5]}... (Total {len(past_order_ids)})")
print(f"GPS Coordinates (tuple)     : {delivery_coordinates}")
print(f"Order Mapping (dict)        : Order #1 -> Rs. {orders_dict[1]}, Order #2 -> Rs. {orders_dict[2]}...")
print(f"Unique Restaurants (set)    : {unique_restaurants}")

# List operations: append() & len()
past_order_ids.append(21)
print(f"\n[List] Appended Order #21. Total Order Count: {len(past_order_ids)}")

# Tuple operations: Unpacking & Indexing
lat, long = delivery_coordinates
print(f"[Tuple] Unpacked Coordinates -> Latitude: {lat}, Longitude: {long}")

# Set operations: add() & membership check ('in')
unique_restaurants.add("Dosa Factory")
is_member = "A2B" in unique_restaurants
print(f"[Set] Added 'Dosa Factory'. Is 'A2B' present? {is_member}")

# Dictionary operations: update() & values() summation
orders_dict.update({21: 490})
total_customer_spend = sum(orders_dict.values())
print(f"[Dict] Updated with Order #21 (Rs. 490). Total Customer Spend: Rs. {total_customer_spend}")

# PHASE 4 : WRAP THE LOGIC IN FUNCTIONS

def calculate_bill(price, qty, discount=0):

    subtotal = price * qty

    discount_amount = subtotal * discount / 100

    final_amount = subtotal - discount_amount

    return final_amount

calculated_bill = calculate_bill(
    item_price,
    quantity
)

discounted_bill = calculate_bill(
    item_price,
    quantity,
    10
)

print("\nBill without Discount: Rs.", calculated_bill)
print("Bill with 10% Discount: Rs.", discounted_bill)

wallet_balance = 500

def apply_coupon(coupon_discount):
    global wallet_balance
    local_promo_code = "FOODEX100"
    wallet_balance += coupon_discount
    print(f"  [Inside apply_coupon] Applied promo code '{local_promo_code}'. Updated Wallet: Rs. {wallet_balance:.2f}")

print(f"Initial Global Wallet Balance: Rs. {wallet_balance:.2f}")
apply_coupon(100.0)
print(f"Global Wallet Balance : Rs. {wallet_balance:.2f}")

def process_order_summary(ord_id, orders_map):

    raw_amount = orders_map.get(ord_id, 0.0)
    savings = raw_amount * 0.10  # 10% savings
    final_amount = raw_amount - savings
    delivery_time_est = 25 if final_amount < 400 else 40  
    return final_amount, savings, delivery_time_est

amt_final, amt_saved, est_time = process_order_summary(7, orders_dict)
print(f"\nOrder #7 Summary -> Final Amt: Rs. {amt_final:.2f} | Savings: Rs. {amt_saved:.2f} | Est Time: {est_time} mins")

full_order_values = list(orders_dict.values())

fee_adjusted = list(map(lambda amt: amt * 1.05, full_order_values))

premium_orders = list(filter(lambda amt: amt > 500.0, fee_adjusted))

total_platform_revenue = functools.reduce(lambda acc, val: acc + val, premium_orders)

print("\n--- Functional Pipeline Results ---")
print(f"Raw Order Amounts                  : {full_order_values[:5]}...")
print(f"After 5% Platform Fee (map)        : {[round(x, 1) for x in fee_adjusted[:5]]}...")
print(f"Premium Orders > Rs. 500 (filter)   : {[round(x, 1) for x in premium_orders]}")
print(f"Total Premium Revenue (reduce)     : Rs. {total_platform_revenue:.2f}")

# PHASE 5 : MODEL THE DATA AS CLASSES

class Restaurant:
    def __init__(self, name, cuisine, rating):
        self.name = name
        self.cuisine = cuisine
        self.set_rating(rating) 

    def display_info(self):
        print(f"  * Restaurant: {self.name:<15} | Cuisine: {self.cuisine:<12} | Rating: {self.get_rating()}/5.0")

    def get_rating(self):
        return self.__rating

    def set_rating(self, rating):
        if 1.0 <= rating <= 5:
            self.__rating = rating
        else:
            print(f"  [Validation Warning] Rating {rating} out of bounds! Must be between 1.0 and 5.")

class Order:
    def __init__(self, restaurant_obj: Restaurant, amount: float):
        self.restaurant = restaurant_obj
        self.amount = amount

    def apply_discount(self, percent: float):
        discount_val = self.amount * (percent / 100.0)
        self.amount -= discount_val
        print(f"  Applied {percent}% discount to order at {self.restaurant.name}. New Amount: Rs. {self.amount:.2f}")

class DeliveryPartner:
    def __init__(self, partner_id: int, name: str):
        self.partner_id = partner_id
        self.name = name

    def calculate_pay(self, distance: float):
        """Base calculation method to be overridden by subclasses."""
        pass

class BikePartner(DeliveryPartner):
    def calculate_pay(self, distance: float):
        # Base pay Rs. 20 + Rs. 10 per km
        return 20.0 + (distance * 10.0)

class CarPartner(DeliveryPartner):
    def calculate_pay(self, distance: float):
        # Base pay Rs. 40 + Rs. 18 per km
        return 40.0 + (distance * 18.0)

rest1 = Restaurant("Spice Villa", "North Indian", 4.5)
rest1.display_info()
rest1.set_rating(6.0) 

order_obj = Order(rest1, 850.0)
order_obj.apply_discount(10.0)

partners = [
    BikePartner(101, "Amit (Bike)"),
    CarPartner(102, "Suresh (Car)"),
    BikePartner(103, "Vikas (Bike)")]

delivery_distance_km = 6.0
print(f"\n--- Polymorphic Delivery Pay Calculation ({delivery_distance_km} km) ---")
for partner in partners:
    pay = partner.calculate_pay(delivery_distance_km)
    print(f"  Partner #{partner.partner_id} ({partner.name:<15}) -> Pay: Rs. {pay:.2f}")

# PHASE 6 : MAKE IT FAIL-SAFE

def place_order(price: float, qty: int):
    if price < 0 or qty < 0:
        raise ValueError(f"Invalid parameters: price (Rs. {price}) and qty ({qty}) cannot be negative!")
    
    total_price = price * qty
    price_per_item = total_price / qty
    return total_price, price_per_item

def execute_safe_order_pipeline(ord_id, price, qty):
    print(f"\nAttempting Order #{ord_id} (Price=Rs. {price}, Qty={qty}):")
    try:
        total, unit_price = place_order(price, qty)
        print(f"  [SUCCESS] Order #{ord_id} placed! Total: Rs. {total:.2f}, Unit Price: Rs. {unit_price:.2f}")
    except ValueError as ve:
        print(f"  [CAUGHT VALUE ERROR] Order #{ord_id} rejected -> {ve}")
    except ZeroDivisionError as zde:
        print(f"  [CAUGHT ZERO DIVISION ERROR] Order #{ord_id} rejected -> Item quantity cannot be zero.")
    except Exception as e:
        print(f"  [CAUGHT UNEXPECTED ERROR] Order #{ord_id} failed -> {type(e).__name__}: {e}")
    finally:
        print("  [AUDIT LOG] Order attempt logged.")

execute_safe_order_pipeline(101, 350.0, 2)  
execute_safe_order_pipeline(102, 400.0, 0)  
execute_safe_order_pipeline(103, -150.0, 1) 

# PHASE 7 : PERSIST THE DATA TO DISK

dataset_20_orders = [
    (1, "Spice Villa", 180, "Hyderabad"),
    (2, "Tandoor Express", 450, "Hyderabad"),
    (3, "Pizza Craft", 320, "Bangalore"),
    (4, "Spice Villa", 150, "Hyderabad"),
    (5, "Burger Hub", 600, "Bangalore"),
    (6, "Tandoor Express", 290, "Hyderabad"),
    (7, "Spice Villa", 850, "Hyderabad"),
    (8, "Pizza Craft", 410, "Bangalore"),
    (9, "Tandoor Express", 220, "Hyderabad"),
    (10, "Burger Hub", 350, "Bangalore"),
    (11, "Spice Villa", 199, "Hyderabad"),
    (12, "Pizza Craft", 540, "Bangalore"),
    (13, "Tandoor Express", 720, "Hyderabad"),
    (14, "Burger Hub", 160, "Bangalore"),
    (15, "Spice Villa", 480, "Hyderabad"),
    (16, "Pizza Craft", 310, "Bangalore"),
    (17, "Tandoor Express", 620, "Hyderabad"),
    (18, "Burger Hub", 270, "Bangalore"),
    (19, "Spice Villa", 510, "Hyderabad"),
    (20, "Pizza Craft", 390, "Bangalore")]

txt_filename = "orders.txt"
with open(txt_filename, "w") as f:
    for oid, rest, amt, cty in dataset_20_orders:
        f.write(f"{oid},{rest},{amt}\n")
print(f"Successfully saved 20 order records to '{txt_filename}'.")

# Read file back and print orders with amount > 400
print(f"\n--- Orders > Rs. 400 read from '{txt_filename}' ---")
with open(txt_filename, "r") as f:
    for line in f:
        parts = line.strip().split(",")
        if len(parts) == 3:
            oid_str, rest, amt_str = parts
            if float(amt_str) > 400:
                print(f"  * Order #{oid_str:<2} | Restaurant: {rest:<15} | Amount: Rs. {amt_str}")

#= Text File Append Mode ('a')
with open(txt_filename, "a") as f:
    f.write("21,Burger Hub,520\n")
print(f"\nAppended Order #21 to '{txt_filename}' without overwriting existing data.")

#  Exporting Tabular Data to CSV & Excel with Pandas
csv_filename = "orders.csv"

df_phase7 = pd.DataFrame(dataset_20_orders, columns=["order_id", "restaurant", "amount", "city"])
df_phase7.to_csv(csv_filename, index=False)
try:
    df_phase7.to_excel("orders.xlsx", index=False)
    print(f"Exported clean dataset to '{csv_filename}' and 'orders.xlsx'.")
except Exception:
    print(f"Exported clean dataset to '{csv_filename}'.")

# Read file back into Python and calculate total amount per restaurant
df_loaded = pd.read_csv(csv_filename)
revenue_per_restaurant = df_loaded.groupby("restaurant")["amount"].sum()
print("\n--- Total Revenue per Restaurant (Pandas Read Back) ---")
for rest_name, rev in revenue_per_restaurant.items():
    print(f"  * {rest_name:<15} : Rs. {rev:.2f}")

