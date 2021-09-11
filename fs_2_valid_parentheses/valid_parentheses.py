def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    left_paren = 0
    right_paren = 0
    for paren in parens:
        if paren == "(":
            left_paren += 1
        if paren == ")":
            right_paren += 1
            if left_paren == 0:
                return False

    return left_paren == right_paren