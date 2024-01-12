print("---WELCOME TO AARROAN'S VENDING MACHINE---\n\n")
MENU=["itemid 144, itemName SNICKERS, PRICE: 5",
     "itemid 96, itemName POTATO CHIPS, PRICE: 12",
     "itemid 100, itemName KITKAT, PRICE: 4",
     "itemid 75, itemName CHEETOS, PRICE: 9.99",
     "itemid 250 itemName PEPSI, PRICE: 2",]
for item in MENU:
    print(item)

items = [
        {"itemid": 144, "itemName": "SNICKERS", "PRICE": 5},
        {"itemid": 96, "itemName": "POTATO CHIPS", "PRICE": 12},
        {"itemid": 100, "itemName": "KITKAT", "PRICE": 4},
        {"itemid": 75, "itemName": "CHEETOS", "PRICE": 9.99},
        {"itemid": 250, "itemName": "PEPSI", "PRICE": 2},]

ITEMS = int(input("ENTER THE ITEMID OF THE ITEM YOU WANT TO PURCHASE:"))
item = None
for i in items:
         if ITEMS == i['itemid']:
           item = i
if item is None:
        print('INVALID CODE')
        
         
else: 
        print(f"GREAT,{item['itemName']} will cost you {item['PRICE']} dollars")


if price == item['PRICE']:
            print(f"THANK FOR YOUR PURCHASE HERE IS YOUR {item['itemName']}")
            print("DO VISIT AGAIN :)")
                
if price < item['PRICE']:
        print("INSUFFICIENT FUNDS. TRANSCATION CANCELLED.")
        
else:
 change = price - item['PRICE']
    
print(f"THANK YOU FOR YOUR PURCHASE. HERE IS YOUR {item['itemName']}")
print(f"Your change is : {change:.2f} dollars")
