from datetime import datetime

name = input("Enter your name: ").upper()
print(f"\nWelcome {name}! Here's the Menu:\n")

items = {
    1: ("PANEER PIZZA 🍕", 119),
    2: ("CORN PIZZA 🍕", 119),
    3: ("TANDOORI PIZZA 🍕", 129),
    4: ("SPICY CHICKEN PIZZA 🍕", 129),
    5: ("CHEESY OCEAN PIZZA 🍕", 199),
    6: ("FRIEDS 2 PCS 🍗", 129),
    7: ("FRIED WINGS 4 PCS 🍗", 109),
    8: ("CHICKEN POPCORN 🍿 (SMALL 110GR)", 119),
    9: ("CHICKEN POPCORN 🍗🍿 (LARGE 220GR)", 229),
    10: ("PANEER SANDWICH 🧀🍿", 49),
    11: ("EGG SANDWICH 🌭", 49),
    12: ("CHICKEN SANDWICH 🌭", 59),
    13: ("CLASSIC BURGER 🍔", 99),
    14: ("PANEER BURGER 🍔", 119),
    15: ("CLASSIC CHICKEN BURGER 🍔", 139),
    16: ("PANEER ROLL 🥖", 79),
    17: ("CLASSIC CHICKEN ROLL 🥖", 89),
    18: ("SPICY CHICKEN ROLL 🥖", 99),
    19: ("VEG RAMEN 🍜", 109),
    20: ("EGG RAMEN 🍜", 159),
    21: ("SPRITE 🥤", 20),
    22: ("THUMPS UP 🥤", 20),
    23: ("MOJITO 🥤", 49),
    24: ("BLACK CURRANT 🥤", 49),
    25: ("BLUE BERRY 🥤", 59),
    26: ("WATER BOTTLE [SMALL]", 10),
    27: ("WATER BOTTLE [BIG]", 20)
}

# Show the menu
print("="*60)
for key, (item_name, price) in items.items():
    print(f"{key}. {item_name} - ₹{price}")
print("="*60)

# Billing variables
totalprice = 0
pricelist = []
ilist = []
qlist = []
plist = []

# Item selection loop
while True:
    choice = int(input("\nEnter item number (0 to finish): "))
    if choice == 0:
        break
    if choice in items:
        item_name, price = items[choice]
        quantity = int(input(f"Enter quantity for {item_name}: "))
        total = price * quantity
        totalprice += total

        # Store details
        pricelist.append((item_name, quantity, price, total))
        ilist.append(item_name)
        qlist.append(quantity)
        plist.append(total)
    else:
        print("Invalid item number!")

# Ask to print bill
confirm = input("\nDo you want to print the bill? (yes/no): ").lower()
if confirm == "yes" and totalprice > 0:
    gst = round(totalprice * 0.05, 2)
    finalamount = totalprice + gst

    print("\n" + "="*35 + " CRISPY CHEESY WORLD " + "="*35)
    print("="*35 + " RUDRAMPETA BYPASS " + "="*36)
    print(f"Name: {name}{' '*40}Date: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
    print("="*100)
    print(f"{'S.No':<6} {'Item':<35} {'Qty':<10} {'Unit Price':<15} {'Total':<10}")
    print("-"*100)

    for idx, (iname, qty, uprice, tprice) in enumerate(pricelist, 1):
        print(f"{idx:<6} {iname:<35} {qty:<10} ₹{uprice:<13} ₹{tprice:<10}")

    print("-"*100)
    print(f"{' '*70}Subtotal: ₹{totalprice}")
    print(f"{' '*70}GST (5%): ₹{gst}")
    print(f"{' '*70}Total Amount: ₹{finalamount}")
    print("="*100)
    print(" " * 35 + "🍽 🤭 THANKS FOR VISITING ❤")
    print(" " * 35 + "🍴 🍽   VISIT AGAIN 🍽 🍴 ")
    print("="*100)
else:
    print("\nThank you! Have a great day!")
