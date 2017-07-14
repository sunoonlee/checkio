from collections import Counter


def checkio(text):
    letters = (char.lower() for char in text if char.isalpha())
    most_common_letters = Counter(letters).most_common()
    result, max_count = most_common_letters[0]
    for letter, count in most_common_letters:
        if count == max_count:
            if letter < result:
                result = letter
        else:
            break
    return result


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
