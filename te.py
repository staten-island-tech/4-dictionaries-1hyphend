print("welcome to barnes and noble, here are the ONLY books we have")
cart=[]
BNBOOKS  = [
{
    "Title":"Dog Man Big Jim Believes",
    "year": 2024,
    "genre": "Fiction",
    "price": 12.99,
    "author": "Dav Pilkey"
    
}, 
{
    "Title":"The Bad Guys",
    "year":2022,
    "genre": "fiction",
    "price": 22.99,
    "author": "Aaron Blabey"

}, 
{
    "Title":"Dog man: A Tale of Two Kitties",
    "year":2017,
    "genre": "fiction",
    "price": 12.99,
    "author": "Dav Pilkey"
},
{
    "Title":"Dog Man: A Graphic Novel",
    "year":2015,
    "genre": "fiction",
    "price": 10.54,
    "author": "Dav Pilkey"
},
{
    "Title":"The Bad Guys in Let the Games Begin!",
    "year":2023,
    "genre": "fiction",
    "price": 22.99,
    "author": "Aaron Blabey"
}
]

for index, BNBOOKS in enumerate(BNBOOKS): 
    print(index, ":", BNBOOKS["Title"])
while True:
    BNBOOKS > 0 
    print("Is that all you want to buy ")
    if BNBOOKS:

        print(index("title"))
        print(index("price"))
# cart = [ ]       
total = 0
shopping = True
while shopping:
    print("Available items:")
    for item in enumerate(store_items):
        print(f"{item['name']}, {item['price']}, ({item['category']})")
    choice = int(input("Enter the number of the item you wish to buy: "))
    selected_item = store_items[choice]
      cart.append(selected_item)
    total += ["price"]
        print(f”Added {selected_item['name']} to your cart.")
    answer = input("Do you want to continue shopping? (yes/no): ")
    if answer != "yes":
        shopping = False
print("cart")
for item in cart:
    print(f"- {item['name']}")
print(f"Total: {total:.2f}")
print("Thank you for shopping with us!")




while True:
    choice = input("What would you like to buy? (or type 'done' to finish): ")

    if choice == 'done':
        break  
    if choice in store:
        quantity = int(input(f"How many {books}s would you like to add? "))
if cart:
    print("Your Cart:")
    total = 0
    for item, quantity in cart.items():
        cost = store[item] * quantity
        total += cost
        print(f"- {item()} x{quantity} = {cost:.2f}")

    print(f" Your Total Amount is: {total:.2f}")
else:
    print("You have to buy something brokie.")

print("Thank you for shopping with us!")
