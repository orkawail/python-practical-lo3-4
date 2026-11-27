# Created by Bence Elmer @ 20/11/26
# Allows for easy defining using classes for products.

from Modules.ProductTypes import *

products : dict[str, productDefinition] = {
    "milk" : {
        "name" : "Bottled Milk",
        "price": 1.85
    },
    "bread" : {
        "name" : "Bread",
        "price": 2.25
    },
    "eggs" : {
        "name" : "Eggs",
        "price": 3.50
    },
    "cheese" : {
        "name" : "Cheese",
        "price": 3.25
    },
    "energy_drink" : {
        "name" : "Monster Energy",
        "price" : 1.99
    },
    "water" : {
        "name" : "Bottle of Water",
        "price" : 0.99
    }
}