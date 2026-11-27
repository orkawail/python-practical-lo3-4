# Created by Bence Elmer @ 20/11/26
# Automatically compiles a dictionary of products from 'products.py'

from inspect import getmembers
from typing import *

# Func imports
from Func.Sort import *

# Modules imports
from Modules.Products import *
from Modules.ProductTypes import *

def getProducts() -> dict:

    productDict : dict = {} # Create a new table
    iteration : int = 0 # Counts the loop iterations

    # Loops through a copy of the original table
    for p in (products.copy().values()): 
        productDict[iteration] = p

        iteration += 1

    productDict = bubble_v2(productDict)

    print("---------------------")
    print("Product list created!")
    print("---------------------")

    return productDict