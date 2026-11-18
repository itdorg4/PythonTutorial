# profile = {"name":"Virat",  
#            "age": 38, 
#            "skills": ["Batting", "Fielding"], 
#            "age": 39}




# print(profile["team"])
# print(profile.get("height"))
# print(profile.get("height", "Key Not Found"))



# print(profile)

# # ordered
# # collection of key value pair

# print(profile[0])


# print(len(profile))


# print(list(profile.keys()))
# print(list(profile.values()))


# out = dict([(["fn", 'ln'], "Virat")])


# print(out)




# profile = {"name":"Virat",
#            "skills": ["Batting", "Fielding"], 
#            "age": 39}



# profile["city"] = "Delhi"

# profile.update({'height': 5.8, "wieght": 65, "skills": ['Reading', "Writing"]})


# # profile.pop('skills')


# profile.popitem()
# profile.popitem()
# profile.popitem()


# print(profile.items())





# update()

# pop()
# popitems()

# clear()


# keys()

# values()

# items()
# setdeault()




profile = {"name":"Virat",
           "skills": ["Batting", "Fielding"], 
           "age": 39}


# print(profile.setdefault("Height", 5.7))


# print(profile)


products = [{
    "id": 1,
    "title": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
    "price": 109.95,
    "description": "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday",
    "category": "men's clothing",
    "image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_t.png",
    "rating": {
      "rate": 3.9,
      "count": 120
    }
  },
  {
    "id": 2,
    "title": "Mens Casual Premium Slim Fit T-Shirts ",
    "price": 22.3,
    "description": "Slim-fitting style, contrast raglan long sleeve, three-button henley placket, light weight & soft fabric for breathable and comfortable wearing. And Solid stitched shirts with round neck made for durability and a great fit for casual fashion wear and diehard baseball fans. The Henley style round neckline includes a three-button placket.",
    "category": "men's clothing",
    "image": "https://fakestoreapi.com/img/71-3HjGNDUL._AC_SY879._SX._UX._SY._UY_t.png",
    "rating": {
      "rate": 4.1,
      "count": 259
    }
  },
  {
    "id": 3,
    "title": "Mens Cotton Jacket",
    "price": 55.99,
    "description": "great outerwear jackets for Spring/Autumn/Winter, suitable for many occasions, such as working, hiking, camping, mountain/rock climbing, cycling, traveling or other outdoors. Good gift choice for you or your family member. A warm hearted love to Father, husband or son in this thanksgiving or Christmas Day.",
    "category": "men's clothing",
    "image": "https://fakestoreapi.com/img/71li-ujtlUL._AC_UX679_t.png",
    "rating": {
      "rate": 4.7,
      "count": 500
    }
  }]


print(products[0].get('price') + products[1].get('price') + products[2].get('price'))

sum = 0
for product in products:
    sum += product.get('price')


print(f"Total is {sum}")