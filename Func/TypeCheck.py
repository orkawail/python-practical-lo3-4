
# Check if number is larger than given number

# Returns true if the number is within the range
def check_num(num : int, min : int, max : int) -> bool:

    if (num < min) or (num > max):
        return False
        
    return True