# Created by Bence Elmer @ 27/11/26
# Calculates the dicount and returns the original and dicounted price

def calculate_price(priceList : list[float]) -> tuple[float, float]:

    if (not isinstance(priceList, list)):
        return

    total : float = 0
    minimum : float = min(priceList)

    for price in (priceList):
        total += price
        
    return total, total - minimum