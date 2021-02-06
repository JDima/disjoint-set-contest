import math

import pytest

from .task import DisjointSet, task1


class Case:
    def __init__(self, name: str, n: int, k: int, m: int, answer: int):
        self._name = name
        self.n = n
        self.k = k
        self.m = m
        self.answer = answer

    def __str__(self) -> str:
        return 'task1_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base1',
        n=1,
        k=1,
        m=1,
        answer=1,
    ),
    Case(
        name='base2',
        n=5,
        k=4,
        m=2,
        answer=2,
    ),
    Case(
        name='base3',
        n=6,
        k=6,
        m=4,
        answer=64,
    ),
    Case(
        name='base4',
        n=7,
        k=7,
        m=3,
        answer=81,
    ),
    Case(
        name='base5',
        n=5,
        k=6,
        m=3,
        answer=0,
    ),
    Case(
        name='base6',
        n=10,
        k=4,
        m=3,
        answer=3,
    ),
    Case(
        name='base7',
        n=10,
        k=3,
        m=5,
        answer=25,
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task1(case: Case) -> None:
    answer = task1(
        n=case.n,
        k=case.k,
        m=case.m,
    )
    assert answer == case.answer
