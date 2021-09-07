def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    result = ""
    words = phrase.split(" ")
    for i in [word.capitalize() for word in words]:
        result += i
        result += " "

    return result[0:len(result)-1:]
