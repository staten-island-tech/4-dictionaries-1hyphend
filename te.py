print("WELCOME TO BARNES AND NOBLES WE ONLY HAVE THESE BOOKS")
cart = [ ]       
total = 0
shopping = [
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

shopping_active = True
while shopping_active:
    print(f"What books would you like to buy: 1. Dog Man: Big Jim believes 2. The Bad Guys 3. Dog man: A Tale of Two Kitties 4. Dog man: A graphic Noveln 5.The Bad Guys in Let the Games Begin!" )
print (input("1,2,3,4,5"))
choice = input("What else would you like to buy? (or type 'done' to finish): ") 
while True:
    if choice == 'done':
        break
    else:
         index = int(choice)
         if 0 != index < len(shopping):
              cart.append(shopping[index])
              print(f" You have added {shopping(index('Title'))}")
    if cart:
        print("You've bought these items:")
    total = 0
    for item, in cart:
        total = sum(shopping[item]['cost'])
        print(f" Your Total Amount is: {total:f}")

    

