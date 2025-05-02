def balancedStringSplit(s):
    count = 0   # To keep track of balance
    result = 0  # Final number of balanced strings

    for char in s:
        if char == 'R':
            count += 1
        else:  # char == 'L'
            count -= 1
        
        if count == 0:
            result += 1  # Found a balanced substring

    return result
