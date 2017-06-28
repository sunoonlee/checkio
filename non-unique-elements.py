from collections import Counter

def checkio(data):
    cnt = Counter(data)
    return [d for d in data if cnt[d] > 1]

#or, use list.count(element) method for counting.