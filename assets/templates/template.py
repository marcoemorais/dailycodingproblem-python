from collections import namedtuple
import unittest


def solution():
    """Description of solution to some problem."""
    pass


class SolutionTest(unittest.TestCase):

    def test_solution(self):
        case = namedtuple('case', ['input','expected'])
        cases = [
            # Insert test cases.
        ]
        for c in cases:
            rcv = solution(c.input)
            self.assertEqual(rcv, c.expected)


unittest.main(SolutionTest(), argv=[''], verbosity=2, exit=False)
