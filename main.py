# Created by Bence Elmer @ 20/11/26
# Main python file.

from Func import Compile, Sort, TypeCheck, List, Calculate

# Modules imports
from Modules.Products import *
from Modules.ProductTypes import *

# Variables
inputCount : int = 0 # Counter for how many inputs have been created
inputProductPrices : list[float] = [] # Contains the prices of the products that have been entered by the user

productDictionary : dict = Compile.getProducts()
productDictionarySize : int = len(productDictionary) - 1 # Removes 1 as dictionary starts at index 0

List.list_products(productDictionary)

# Main loop to accept inputs
while inputCount < 5:

    # Sanity check to ensure no extra products are bugged into the list
    if (inputCount < 0):
        inputCount = 0

    # Deciding which prompt to use
    if (inputCount == 0):
        print("---------------------")
        inp = input("Please select a product by typing it's ID (Left hand side): ")
        print("---------------------")
    else:
        inp = input("Please select another product: ")
        print("---------------------")

    # Conversion and type checking
    try: # Attempt to convert to a float
        inp = float(inp)
    except:
        print("Please enter a valid input type!")
        inputCount -= 1
    else:
        id = float(inp)

        validNum = TypeCheck.check_num(id, 0, productDictionarySize) # Run a quick check that number is within acceptable range

        if (validNum == False): # If the number is not valid
            print("Please enter a valid input type!")
            inputCount -= 1

            continue
        
        # Adding all the prices of each item to a seperate list
        product : productDefinition = productDictionary[id]

        for i, val in (product.items()):
            if (i != "price"):
                continue

            inputProductPrices.append(val)

    inputCount += 1

# Obtaining full price and the dicounted price
fullPrice, discountedPrice = Calculate.calculate_price(inputProductPrices)

# Outputting the prices
print("---------------------")
print(f"Your total price comes to: £{fullPrice}")
print("---------------------")
print(f"Your total price, with the cheapest item free is: £{discountedPrice}")
print("---------------------")