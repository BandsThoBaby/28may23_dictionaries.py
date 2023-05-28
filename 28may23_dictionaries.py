"""
Dictionaries store data values in key:value pairs.
Example:

"""
my_first_dictionary = {
    "brand": "Yamaha",
    "model": "Aerox",
    "year": 2021
}

print(my_first_dictionary)

# Dictionary items are ordered, changeable and do not allow for duplicates.

# Dictionary items are presented in key:value pairs.

# They can be referred to by using the key name. 

my_second_dictionary = {
  "brand": "Kawasaki",
  "model": "Ninja 400",
  "year": 2023
}
print(my_second_dictionary["brand"])

# The above code prints only the brand value of the dictionary. 

# Dictionaries cannot have two items with the same key.

# Use the len function to determine how many items a list has. (See below)

print(len(my_second_dictionary))



# Dictionaries are objects with the data type 'dict'

# <class 'dict'>

# Below is how to print determine and print the data type :

moto_gp_buriram = {
    "race_name": "Buriram Grand Prix",
    "date": "October 15th, 2023",
    "location": "Buriram, Thailand"
}

print(type(moto_gp_buriram))

# It is also possible to construct a dictionary with the dict() constructor:

south_london_postcodes = dict(postcode = "SW2", name = "Brixton", borough = "Lambeth")
print(south_london_postcodes)