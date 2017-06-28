def checkio(matrix):
    n = len(matrix)

    # horizontal
    for row in matrix:
        count = 1
        for col in range(n-1):
            if row[col+1] == row[col]:
                count += 1
                if count == 4: return True
            else: count = 1

    # vertical
    for col in range(n):
        count = 1
        for row in range(n-1):
            if matrix[row+1][col] == matrix[row][col]:
                count += 1
                if count == 4: return True
            else: count = 1

    # diagnal NW-SE
    for i in range(n):
        count = 1
        for j in range(n-i-1):
            if matrix[i+j][j] == matrix[i+j+1][j+1]:
                count += 1
                if count == 4: return True
            else: count = 1

    for j in range(1, n):
        count = 1
        for i in range(n-j-1):
            if matrix[i][i+j] == matrix[i+1][i+j+1]:
                count += 1
                if count == 4: return True
            else: count = 1

    # diagnal NE-SW
    for i in range(n):
        count = 1
        for j in range(i):
            if matrix[i-j][j] == matrix[i-j-1][j+1]:
                count += 1
                if count == 4: return True
            else: count = 1

    for j in range(1, n):
        count = 1
        for i in range(n-1, j, -1):
            if matrix[i][j+n-i-1] == matrix[i-1][j+n-i]:
                count += 1
                if count == 4: return True
            else: count = 1

    return False

if __name__ == '__main__':
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
