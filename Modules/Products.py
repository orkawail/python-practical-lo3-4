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
    },
    "apple": {
        "name": "Apple",
        "price": 0.50
    },
    "banana": {
        "name": "Banana",
        "price": 0.30
    },
    "orange": {
        "name": "Orange",
        "price": 0.45
    },
    "crisps": {
        "name": "Potato Crisps",
        "price": 1.25
    },
    "choc": {
        "name": "Milk Chocolate",
        "price": 1.10
    },
    "cola": {
        "name": "Classic Coca-Cola",
        "price": 1.50
    },
    "juice": {
        "name": "Fresh Orange Juice",
        "price": 1.80
    },
    "pasta": {
        "name": "Dried Penne Pasta",
        "price": 1.20
    },
    "rice": {
        "name": "Long Grain White Rice",
        "price": 1.60
    },
    "sugar": {
        "name": "Granulated White Sugar",
        "price": 1.30
    },
    "salt": {
        "name": "Table Salt",
        "price": 0.80
    },
    "coffee": {
        "name": "Coffee",
        "price": 3.50
    },
    "tea": {
        "name": "Tea",
        "price": 2.20
    },
    "butter": {
        "name": "Butter",
        "price": 2.10
    },
    "yogurt": {
        "name": "Natural Greek Yogurt",
        "price": 1.75
    },
    "chicken": {
        "name": "Chicken Breast",
        "price": 4.50
    },
    "beef": {
        "name": "Beef Mince",
        "price": 4.00
    },
    "potato": {
        "name": "Potato",
        "price": 0.70
    },
    "carrot": {
        "name": "Carrots",
        "price": 0.90
    },
    "tomato": {
        "name": "Tomatoes",
        "price": 1.40
    }
}