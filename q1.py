def swap_values(x, y):
    # Check if both x and y are numeric
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1
    
    # Swap using only x and y
    x = x + y
    y = x - y
    x = x - y
    
    # Print swapped values
    print("Swapped x =", x)
    print("Swapped y =", y)

# Example usage
print (swap_values("Apple", 10)) # -1
print (swap_values(9, 17))  # Swapped x = 17, Swapped y = 9
