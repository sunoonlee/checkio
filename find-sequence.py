def checkio(matrix):
    n = len(matrix)

    # horizontal
    for row in matrix:
        count = 1
        for j in range(n-1):
            if row[j+1] == row[j]:
                count += 1
                if count == 4: return True
            else: count = 1

    # vertical
    for j in range(n):
        count = 1
        for i in range(n-1):
            if matrix[i+1][j] == matrix[i][j]:
                count += 1
                if count == 4: return True
            else: count = 1

    # diagnal NW-SE
    for i in range(n):
        row = i
        col = 0
        count = 1
        for j in range(n-1-i):
            if matrix[row][col] == matrix[row+1][col+1]:
                count += 1
                if count == 4: return True
            else: count = 1
            row += 1
            col += 1

    for i in range(1, n):
        row = 0
        col = i
        count = 1
        for j in range(n-1):
            if not (0 <= row < n-1 and 0 <= col < n-1): break
            if matrix[row][col] == matrix[row+1][col+1]:
                count += 1
                if count == 4: return True
            else: count = 1
            row += 1
            col += 1

    # diagnal NE-SW
    for i in range(n):
        row = i
        col = 0
        count = 1
        for j in range(n-1):
            if not (1 <= row < n and 0 <= col < n-1): break
            if matrix[row][col] == matrix[row-1][col+1]:
                count += 1
                if count == 4: return True
            else: count = 1
            row -= 1
            col += 1

    for i in range(1, n):
        row = n - 1
        col = i
        count = 1
        for j in range(n-1):
            if not (1 <= row < n and 0 <= col < n-1): break
            if matrix[row][col] == matrix[row-1][col+1]:
                count += 1
                if count == 4: return True
            else: count = 1
            row -= 1
            col += 1

    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
