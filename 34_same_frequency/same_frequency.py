def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    # I dont know why integers are not that operatable upon when they could easily be.

    if len(str(num1)) < len(str(num2)):
        return False

    a = [int(x) for x in str(num1)].sort()
    b = [int(x) for x in str(num2)].sort()

    return a == b