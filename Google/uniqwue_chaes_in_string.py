def remove_min_substring(string):
# Initialize variables
start = 0
end = 0
max_length = 0
longest_substring = ""

# Dictionary to store the last seen index of a character
char_index = {}

# Iterate through the string
while end < len(string):
    # If the character is already in char_index and its last occurrence is after start
    if string[end] in char_index and char_index[string[end]] >= start:
        # Update start to the index after the last occurrence of the character
        start = char_index[string[end]] + 1

    # Update the last seen index of the character
    char_index[string[end]] = end

    # If the length of the current substring is greater than the maximum length found so far
    if end - start + 1 > max_length:
        max_length = end - start + 1
        longest_substring = string[start:end + 1]

    # Move to the next character
    end += 1

# Calculate the number of characters to remove
chars_to_remove = len(string) - max_length

return chars_to_remove, longest_substring
