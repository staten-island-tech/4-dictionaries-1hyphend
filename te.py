# print("WELCOME TO BARNES AND NOBLES WE ONLY HAVE THESE BOOKS")
# cart = [ ]       
# cost = ("price")
# shopping = [
#     {
#     "Title":"Dog Man Big Jim Believes",
#     "year": 2024,
#     "genre": "Fiction",
#     "price": 12.99,
#     "author": "Dav Pilkey"
    
# }, 
# {
#     "Title":"The Bad Guys",
#     "year":2022,
#     "genre": "fiction",
#     "price": 22.99,
#     "author": "Aaron Blabey"

# }, 
# {
#     "Title":"Dog man: A Tale of Two Kitties",
#     "year":2017,
#     "genre": "fiction",
#     "price": 12.99,
#     "author": "Dav Pilkey"
# },
# {
#     "Title":"Dog Man: A Graphic Novel",
#     "year":2015,
#     "genre": "fiction",
#     "price": 10.54,
#     "author": "Dav Pilkey"
# },
# {
#     "Title":"The Bad Guys in Let the Games Begin!",
#     "year":2023,
#     "genre": "fiction",
#     "price": 22.99,
#     "author": "Aaron Blabey"
# }
# ]

# for index, item in enumerate(shopping):
#         print(index, ":", item["Title"])

# while True:
#     if shopping==True:
#         print("What books would you like to buy: 1. Dog Man: Big Jim believes 2. The Bad Guys 3. Dog man: A Tale of Two Kitties 4. Dog man: A graphic Noveln 5.The Bad Guys in Let the Games Begin!" )
#     print (input("1,2,3,4,5"))
#     choice = input("What else would you like to buy? (or type 'done' to finish): ") 
#     if choice == 'done':
#         print(f"You've bought these items:{index}")
    
#         index = (choice)
#         if 0 == index < len(shopping):
#             cart.append(shopping[index])
#         for item in cart:
#             total = sum([cost])
#         print(f" Your Total Amount is:{total}")





# numero duo 

# from movies_data import movies

# year = int(input("Enter a year: "))

# print(f"\nMovies released after {year}:")
# for movie in movies:
#     if movie["year"] > year:
#         print(f"{movie['title']} ({movie['year']})")


# numero thres 
# from movies_data import movies

# start_year = int(input("Enter start year: "))
# end_year = int(input("Enter end year: "))

# print(f"\nMovies released between {start_year} and {end_year}:")
# for movie in movies:
#     if start_year < movie["year"] < end_year:
#         print(f"{movie['title']} ({movie['year']})")


# numero quarter 

from movies_data import movies

year = int(input("Enter a year: "))

print(f" (Movies released in {year}):")
for movie in movies:
    if movie["year"] == year:
        print(f"{movie['title']} ({movie['genre']})")

# numebr feive 

# search = input()
# from movies_data import movies

# def search_movie(title):
#     search = (for m in movies if title.lower() in m["title"].lower())
#     return search
