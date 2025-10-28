print("welcome to barnes and noble, what are you buying today")

Barnes_noble_books = [
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
    "Title":"The Bad Guys",
    "year":2022,
    "genre": "fiction",
    "price": 22.99,
    "author": "Aaron Blabey"
},
{
    "Title":"Dog Man: A Graphic Novel",
    "year":2022,
    "genre": "fiction",
    "price": 10.54,
    "author": "Aaron Blabey"
},
{
    "Title":"The Bad Guys in Let the Games Begin!",
    "year":2023,
    "genre": "fiction",
    "price": 22.99,
    "author": "Aaron Blabey"
}
]

for index, Barnes_noble_books in enumerate(Barnes_noble_books):
    print(index, ":", Barnes_noble_books["Title"])