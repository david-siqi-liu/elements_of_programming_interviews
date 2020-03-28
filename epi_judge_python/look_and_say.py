from test_framework import generic_test


def look_and_say(n: int) -> str:
    if n == 1:
        return '1'

    result = []
    prev = look_and_say(n - 1)
    count = 1
    slow = 0
    for fast in range(1, len(prev)):
        if prev[fast] == prev[slow]:
            count += 1
        else:
            result.append(str(count))
            result.append(prev[slow])
            slow = fast
            count = 1

    result.append(str(count))
    result.append(prev[slow])

    return ''.join(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
