from test_framework import generic_test


def evaluate(expression: str) -> int:
    partials = []

    OPERATORS = {
        '+': lambda y, x: x + y,
        '-': lambda y, x: x - y,
        '*': lambda y, x: x * y,
        '/': lambda y, x: int(x / y)
    }

    for token in expression.split(','):
        if token in OPERATORS:
            y = partials.pop()
            x = partials.pop()
            result = OPERATORS[token](y, x)
            partials.append(result)
        else:
            partials.append(int(token))

    return partials[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
