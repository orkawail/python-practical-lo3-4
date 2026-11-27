# Created by Bence Elmer @ 27/11/26
# Prints all the items in a list

def list_products(productDictionary : dict):
    
    # Type checking
    if (not isinstance(productDictionary, dict)):
        return

    # Main loop
    for i, product in (productDictionary.items()):
        name : str = None
        price : float = None

        for j, val in (product.items()):
            if (j == "name"):
                name = val

            if (j == "price"):
                price = val

        print(f"id: {i}", " | ", f"item: {name}", " | ",f"price: {price}")