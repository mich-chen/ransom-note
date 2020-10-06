def checkMagazine(magazine, note):
    """Return boolean if magazine has all whole words for ransom note."""

    words = {}

    for word in magazine.split():
        words.setdefault(word, 0)
        words[word] += 1

    # decrement any ransom words that are in magazine words
    for word in note.split():
        if word in words:
            words[word] -= 1
        # if ransom word is not in magazine words, then return False
        else:
            return False

    # if any leftover magazine words are negative, meaning ransom words had more
    # then return False because magazine didn't have enough
    for value in words.values():
        if value < 0:
            return False

    return True



"""
Alternative Solution: Counter

def checkMagazine(magazine, note):

    from collections import Counter

    # use Counter method
    return ((Counter(note.split()) - Counter(magazine).split()) == {})

"""


"""
Alternative Solution:

def checkMagazine(magazine, note):

    magazine_set = set(magazine.split())

    ransom_words = note.split()
    for word in ransom_words:
        if word not in magazine_set:
            return False
  
    return True
"""


if __name__ == '__main__':

    m1 = "give me one grand today night"
    n1 = "give one grand today"
    print(checkMagazine(m1, n1))  # True

    m2 = "ive Got a Lovely Bunch of Coconuts"
    n2 = "ive got some coconuts"
    print(checkMagazine(m2, n2))  # False

    m3 = "there are two pigeons and doves here now"
    n3 = "two pigeons and two doves now"
    print(checkMagazine(m3, n3))  # False
