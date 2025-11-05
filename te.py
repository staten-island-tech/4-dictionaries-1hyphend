print("WELCOME TO BARNES AND NOBLES WE ONLY HAVE THESE BOOKS")
cart = [ ]       
total = 0
shopping= [
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
for index, item in enumerate(shopping):
        print(index, ":", item["Title"])
while shopping==True:
    print(f"What books would you like to buy: 1. Dog Man: Big Jim believes 2. The Bad Guys 3. Dog man: A Tale of Two Kitties 4. Dog man: A graphic Noveln 5.The Bad Guys in Let the Games Begin!" )
print (input("1,2,3,4,5"))
choice = int(input("Enter the number of the item you wish to buy: "))
selected_item = cart[choice]
cart.append(shopping)
total += selected_item["price"]

answer = input("Do you want to continue shopping? (yes/no): ")
if answer != "yes":
        shopping = False
print(cart)
for item in cart:
    print(f"-{item['title']}")
print(f"Total:{total:.2f}")
print("Thank you for shopping with us!")