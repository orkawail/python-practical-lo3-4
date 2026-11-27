# Created by Bence Elmer @ 20/11/26
# Uses sorting algorithms to sort the product dictionaries.

# Modules imports
from Modules import Products
from Modules.ProductTypes import *

def bubble_v2(productDict: dict):

    swapped : bool = True # Variable to track if anything has been swapped

    previousPrice : float = 0 # Previous price
    previousProduct : productDefinition = None

    keys : list = [] # List of keys to identify products with

    while swapped: # Repeat while things are swapping

        # Resetting flags
        swapped = False

        previousProduct = None
        previousPrice = 0
        previousKey = 0

        keys = productDict.keys()

        for i, (key) in enumerate(keys):
            currentProduct = productDict[key]
            currentPrice = currentProduct["price"]
            currentKey = key

            if (i == 0): # First iteration
                previousProduct = currentProduct
                previousPrice = currentPrice
                previousKey = currentKey

                continue

            if (previousPrice < currentPrice):
                productDict[previousKey], productDict[currentKey] = productDict[currentKey], productDict[previousKey]

                swapped = True

            previousProduct = currentProduct
            previousPrice = currentPrice
            previousKey = currentKey
            
    print("---------------------")
    print("Product list sorted!")
    print("---------------------")

    return productDict



