# Created by Bence Elmer @ 20/11/26
# Automatically compiles a dictionary of products from 'products.py'

from inspect import getmembers

# Func imports
from Func.Sort import *

# Modules imports
from Modules import Products
from Modules.ProductTypes import *

def getProducts() -> productDictionaryDefinition:
    productDict : productDictionaryDefinition = {}
    iteration : int = 0 # Custom iteration for key values

    for i, product in getmembers(Products):
        if (isinstance(product, dict)):
            productDict[iteration] = product

            iteration += 1

    productDict = bubble_v2(productDict)

    print("---------------------")
    print("Product list created!")
    print("---------------------")

    return productDict