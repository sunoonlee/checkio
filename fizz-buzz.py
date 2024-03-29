def checkio(number):
    if number % 15 == 0:
        ans = 'Fizz Buzz'
    elif number % 3 == 0:
        ans = 'Fizz'
    elif number % 5 == 0:
        ans = 'Buzz'
    else:
        ans = str(number)
    return ans


if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
