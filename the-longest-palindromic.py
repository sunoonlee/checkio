def is_palindromic(text):
    if len(text) == 0 or len(text) == 1:
        return True
    else:
        return (text[0] == text[-1]) and is_palindromic(text[1:-1])


def longest_palindromic(text):
    N = len(text)
    for len_ in range(N, 1, -1):
        for start in range(0, N-len_+1):
            if is_palindromic(text[start:start+len_]):
                return text[start:start+len_]
    return text[0]


if __name__ == '__main__':
    assert is_palindromic('') == True
    assert is_palindromic('s') == True
    assert is_palindromic('sdds') == True
    assert is_palindromic('abdba') == True

    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
