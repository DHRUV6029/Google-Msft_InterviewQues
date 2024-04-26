def generate_byte_sequences(input_str, min_length=1, max_length=4):
    byte_set = set()

    # Generate byte sequences of length min_length to max_length
    for length in range(min_length, max_length + 1):
        for i in range(len(input_str) - length + 1):
            byte_set.add(input_str[i:i + length])

    return byte_set

def find_shortest_non_present_sequence(input_str):
    byte_set = generate_byte_sequences(input_str)
    
    # Iterate through all possible byte sequences of length 1 to 4
    for length in range(1, 5):
        for i in range(256 ** length):
            byte_sequence = bytes([i >> (8*j) & 0xff for j in range(length)])
            if byte_sequence not in byte_set:
                return byte_sequence.decode('latin-1')  # Convert bytes to string
    
    return ""  # Should not reach here if input is bounded by 4GB

# Test the function
input_str = "abcdefacbeddefd"
result = find_shortest_non_present_sequence(input_str)
print("Shortest non-present sequence:", result)
