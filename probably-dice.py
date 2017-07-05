from math import factorial

def nCr(n, r):
    return factorial(n) / factorial(r) / factorial(n-r)

def probability(n, s, t):
    """
    n: dice number
    s: sides
    t: target total
    formula: http://mathworld.wolfram.com/Dice.html
    """
    if t < n or t > n * s:
        return 0
    kmax = (t-n) // s
    return sum((-1)**k * nCr(n, k) * nCr(t-s*k-1, n-1) 
               for k in range(0, kmax+1)) / s**n

if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision
        
    assert(almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    assert(almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    assert(almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    assert(almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    assert(almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    assert(almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    assert(almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"
