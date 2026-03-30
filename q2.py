def find_and_replace(lst, find_val, replace_val):
    # Check if lst is a list
    if not isinstance(lst, list):
        return -1
    
    # Replace all occurrences of find_val with replace_val
    for i in range(len(lst)):
        if lst[i] == find_val:
            lst[i] = replace_val
    
    return lst

# Example usage
print(find_and_replace([1, 2, 3, 4, 2, 2], 2, 5))
# Output: [1, 5, 3, 4, 5, 5]

print(find_and_replace(["apple", "banana", "apple"], "apple", "orange"))
# Output: ['orange', 'banana', 'orange']
