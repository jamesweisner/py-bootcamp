OPERATORS = [
    ['-', lambda a, b: a - b],
    ['+', lambda a, b: a + b],
    ['/', lambda a, b: a / b],
    ['*', lambda a, b: a * b],
]


def calc(e):
    """
        Returns float value of an expression string e.
        Uses recursion to obeys oerder of operations.
        Limited to integer inputs & "MDAS" operations.
    """
    for op, func in OPERATORS:
        if op in e:
            a, b = e.split(op, 1)
            return func(calc(a), calc(b))
    return int(e)
