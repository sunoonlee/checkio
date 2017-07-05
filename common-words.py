def checkio(first, second):
    words_first = set(first.split(','))
    words_second = set(second.split(','))
    common_words = words_first & words_second
    return ",".join(sorted(common_words))  # sorted() receives any iterable and returns a list

if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
