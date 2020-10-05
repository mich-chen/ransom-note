def checkMagazine(magazine, note):
    """Return boolean if magazine has all whole words for ransom note."""

    magazine_set = set(magazine.split())

    ransom_words = note.split()
    for word in ransom_words:
        if word not in magazine_set:
            return False
  
    return True


if __name__ == '__main__':

    m1 = "give me one grand today night"
    n1 = "give one grand today"
    print(checkMagazine(m1, n1))  # True

    m2 = "ive Got a Lovely Bunch of Coconuts"
    n2 = "ive got some coconuts"
    print(checkMagazine(m2, n2))  # False
