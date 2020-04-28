import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))

# def find_max_simultaneous_events(A: List[Event]) -> int:
#     if not A:
#         return 0
#
#     endpoints_start = [a.start for a in A]
#     endpoints_finish = [a.finish for a in A]
#
#     endpoints_start.sort()
#     endpoints_finish.sort()
#
#     concurrent = [0] * (endpoints_finish[-1] + 1)
#
#     for e in endpoints_start:
#         concurrent[e:] = map(lambda x: x + 1, concurrent[e:])
#
#     for e in endpoints_finish:
#         concurrent[e + 1:] = map(lambda x: x - 1, concurrent[e + 1:])
#
#     return max(concurrent)


Endpoint = collections.namedtuple("Endpoint", ('time', 'is_start'))


def find_max_simultaneous_events(A: List[Event]) -> int:
    E = [Endpoint(event.start, True) for event in A] + [Endpoint(event.finish, False) for event in A]
    E.sort(key=lambda e: (e.time, not e.is_start))

    max_num, curr_num = 0, 0

    for e in E:
        if e.is_start:
            curr_num += 1
            max_num = max(max_num, curr_num)
        else:
            curr_num -= 1

    return max_num


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events,
                                          events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
