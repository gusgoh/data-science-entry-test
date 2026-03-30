def update_dictionary(dct, key, value):
    # Check if dct is a dictionary
    if not isinstance(dct, dict):
        return -1
    
    # If key exists, print original value
    if key in dct:
        print("Original value:", dct[key])
    
    # Update or add the key-value pair
    dct[key] = value
    
    # Return the updated dictionary
    return dct

# Example usage
print(update_dictionary({}, "name", "Alice"))
# Output:
# {'name': 'Alice'}


print(update_dictionary({"age": 25}, "age", 26))
# Output:
# Original value: 25
# {'age': 26}
