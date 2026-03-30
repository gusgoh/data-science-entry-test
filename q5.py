def check_divisiblity(num, divisor):
    # Check if both num and divisor are numeric
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        return -1
    
    # Avoid division by zero
    if divisor == 0:
        return False
    
    # Check divisibility
    return num % divisor == 0

# Example usage
print(check_divisiblity(10, 2))  # Output: True
print(check_divisiblity(7, 3))   # Output: False
