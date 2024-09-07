def hamming_weight(n):
    
    return bin(n).count('1')

# Example usage
n = 29  # Binary representation: 11101
result = hamming_weight(n)
print("Number of set bits (Hamming weight):", result)
