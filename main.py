# Created by Bence Elmer @ 20/11/26
# Main python file.

from Func import Compile, Sort, TypeCheck, List

# Modules imports
from Modules.Products import *
from Modules.ProductTypes import *

# Variables
inputCount : int = 0 # Counter for how many inputs have been created

inputProductPrices : list[float] = [] # Contains the prices of the products that have been entered by the user
inputProductTotalPrice : float = 0 # Contains the total price of all of the products

productDictionary : dict = Compile.getProducts()
productDictionarySize : int = len(productDictionary)

List.list_products(productDictionary)

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
        validNum = TypeCheck.check_num(id, 0, productDictionarySize)
        print(productDictionarySize)

        if (validNum == False):
            print("Please enter a valid input type!")
            inputCount -= 1

            continue

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