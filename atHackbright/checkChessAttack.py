def check(king, queen):
    """
    >>> check("D6", "H6")
    True

    >>> check("E6", "E4")
    True

    >>> check("B7", "D5")
    True

    >>> check("A1", "H8")
    True

    >>> check("A8", "H1")
    True

    >>> check("D6", "H7")
    False

    >>> check("E6", "F4")
    False
    """

    if king[0] == queen[0] or king[1] == queen[1]:
        return True

    king = (ord(king[0]) - ord("A")+1, int(king[1]))
    queen = (ord(queen[0]) - ord("A")+1, int(queen[1]))





    if abs(king[0] - queen[0]) == abs(king[1] - queen[1]):
        return True
    else:
        return False








if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. EXCELLENT GAME!\n"

