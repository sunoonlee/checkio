def checkio(data): 
    ones = ('I', 'X', 'C', 'M')
    fives = ('V', 'L', 'D')
    
    result = []
    j = 0  # position in a base-10 digit
    while data != 0:     
        i = data % 10  # current digit
        current = ''  # roman numeral for current digit
        if i == 9:
            current += ones[j] + ones[j + 1]
        elif i == 4:
            current += ones[j] + fives[j]
        else:
            if i >= 5:
                current += fives[j]
                i -= 5 
            if i in (1, 2, 3):
                current += ones[j] * i
        result.insert(0, current)  
        data = int(data / 10)
        j += 1
    
    return ''.join(result)