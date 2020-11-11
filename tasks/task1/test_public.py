import pytest

from .task import task1


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
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task1(case: Case) -> None:
    answer = task1(
        n=case.n,
        k=case.k,
        m=case.m,
    )
    assert answer == case.answer
