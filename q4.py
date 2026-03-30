def string_reverse(s):
   # Check if s is a string
    if not isinstance(s, str):
        return -1
    
    # Reverse the string
    return s[::-1]

# Example usage
print(string_reverse("Hello World"))   # Output: dlroW olleH
print(string_reverse("Python"))  # Output: nohtyP
