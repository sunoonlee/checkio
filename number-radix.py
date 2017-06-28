"""better: int(str_, base)"""


def char2digit(char):
    if "0" <= char <= "9":
        return int(char)
    if "A" <= char <= "Z":
        return ord(char) - ord('A') + 10

def checkio(str_number, radix):
    result = 0
    position = 0
    for char in str_number[::-1]:
        digit = char2digit(char)
        if digit >= radix:
            return -1
        result += digit * (radix ** position)
        position += 1
    return result


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A > 10"
