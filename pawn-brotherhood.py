def safe_pawns(pawns):
    plist = list(pawns)
    l = len(pawns)
    is_safe = [0] * l

    for i in range(l):
        for j in range(i+1, l):
            d0 = ord(plist[j][0]) - ord(plist[i][0])  # horizontal distance
            d1 = ord(plist[j][1]) - ord(plist[i][1])  # vertical distance
            if d0 in (-1, 1):
                if d1 == 1:
                    is_safe[j] = 1
                elif d1 == -1:
                    is_safe[i] = 1

    return sum(is_safe)
