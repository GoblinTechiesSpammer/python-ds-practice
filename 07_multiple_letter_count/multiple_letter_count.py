def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    letterFreq = {}
    for letter in phrase:
        if letter not in letterFreq:
            letterFreq[letter] = 1
        else:
            letterFreq[letter] += 1
    
    return letterFreq