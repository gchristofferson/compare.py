from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""

    # split each string into lines
    splitA = a.splitlines()
    splitB = b.splitlines()
    # add similar lines to a set, removing duplicates
    similar = {x for x in splitA for y in splitB if x == y}
    # return list that contains all the lines that are present in strings a and b
    return [x for x in similar]


def sentences(a, b):
    """Return sentences in both a and b"""

    # split each string into sentences
    splitA = sent_tokenize(a)
    splitB = sent_tokenize(b)
    # add similar sentences to a set, removing duplicates
    similar = {x for x in splitA for y in splitB if x == y}
    # return list that contains all the sentences that are present in strings a and b
    return [x for x in similar]


def substring(a, n):
    """Return substrings of length n in a"""

    # preserve substring length
    sn = n
    # split string into substrings
    substrings = list()
    length = len(a)
    for i in range(length):
        if len(a[i:n]) == sn:
            substrings.append(a[i:n])
            i += 1
            n += 1
    return substrings


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    # split each string into substrings
    splitA = substring(a, n)
    splitB = substring(b, n)
    # add similar substrings to a set, removing duplicates
    similar = {x for x in splitA for y in splitB if x == y}
    # return a list all the substrings that are present in strings a and b
    return [x for x in similar]