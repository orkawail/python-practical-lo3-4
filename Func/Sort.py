# Created by Bence Elmer @ 20/11/26
# Uses sorting algorithms to sort the product dictionaries.

# Modules imports
from Modules import Products
from Modules.ProductTypes import *

def bubble_v2(productDict: productDictionaryDefinition):

    swapped : bool = True # Variable to check if anything has been swapped
    prevPrice : float = 0

    while swapped: # Repeat while things are swapping
        # Resetting variables
        swapped = False
        prevPrice = 0

        for i, product in (productDict.items()): # Loop through all the products

            for j, val in product.items(): # Loop through the values in the product

                if (j != "price"): # If it is not a price variable, next iteration
                    continue

                curPrice = val

                if (prevPrice > curPrice): # If the value before is larger than the value now, swap positions
                    productDict[i], productDict[i-1] = productDict[i-1], productDict[i]

                    swapped = True

                prevPrice = curPrice

    print("---------------------")
    print("Product list sorted!")
    print("---------------------")

    return productDict



