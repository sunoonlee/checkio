def checkio(data):
    if not data:
        return 0
    else:
        return data.pop() + checkio(data)

if __name__ == '__main__':
    assert checkio([2,3,4]) == 9