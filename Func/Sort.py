# Created by Bence Elmer @ 20/11/26
# Uses sorting algorithms to sort the product dictionaries.

# Modules imports
from Modules import Products
from Modules.ProductTypes import *

def bubble_v2(productDict: dict):

    swapped : bool = True # Variable to track if anything has been swapped
    prevPrice : float = 0 # Previous price
    iterations : int = 0 # Track iterations

    while swapped: # Repeat while things are swapping

        # Resetting flags
        swapped = False
        prevPrice = 0

        #print(productDict)

        # Main loop
        for i, (key, product) in enumerate(productDict.items()): # Loop through all the products
            # Skip iteration if it is the first iteration
            if (i <= 0):
                continue

            try:
                curPrice = product["price"]
            except:
                print("Incorrect price value!")
                continue
            else:
                curPrice = product["price"]

                if (prevPrice < curPrice): # If the value before is smaller than the value now, swap positions
                    productDict[i], productDict[i-1] = productDict[i-1], productDict[i]

                    swapped = True

            prevPrice = curPrice
            
            

            

    print("---------------------")
    print("Product list sorted!")
    print("---------------------")

    return productDict



