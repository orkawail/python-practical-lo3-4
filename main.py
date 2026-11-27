# Created by Bence Elmer @ 20/11/26
# Main python file.

from Func import Compile, Sort

# Modules imports
from Modules import Products
from Modules.ProductTypes import *

# Variables
inputs : list[int] = [] # Defines a list of integers
inputCount : int = 0 # Counter for how many inputs have been created

inputProductPrices : list[float] = [] # Contains the prices of the products that have been entered by the user
inputProductTotalPrice : float = 0

# Main Body
productDictionary : productDictionaryDefinition = Compile.getProducts()

for i, product in (productDictionary.items()):
    name : str = None
    price : float = None

    for j, val in (product.items()):
        if (j == "name"):
            name = val

        if (j == "price"):
            price = val

    print(f"id: {i}", " | ", f"item: {name}", " | ",f"price: {price}")

# Main loop to accept inputs
while inputCount < 5:
    if (inputCount == 0):
        print("---------------------")
        inp = input("Please select a product by typing it's ID (Left hand side): ")
        print("---------------------")
    else:
        inp = input("Please select another product: ")
        print("---------------------")

    try:
        inp = float(inp)
    except:
        print("Please enter a valid input type!")
        inputCount -= 1
    else:
        id = float(inp)
        product : productDefinition = productDictionary[id]

        for i, val in (product.items()):
            if (i != "price"):
                continue

            inputProductPrices.append(val)

    inputCount += 1

# Removing the smallest value
minPrice = min(inputProductPrices)
inputProductPrices.remove(minPrice)

# Loops through and adds up the prices
for price in (inputProductPrices):
    inputProductTotalPrice += price

print("---------------------")
print(f"Your total price, without any discount comes to: £{inputProductTotalPrice + minPrice}")
print("---------------------")
print(f"Your total price, with the cheapest item free is: £{inputProductTotalPrice}")
print("---------------------")
# Loop through all the items and combine their prices into a new table