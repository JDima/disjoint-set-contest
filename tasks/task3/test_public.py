import pytest

from .task import task3


class Case:
    def __init__(self, name: str, k: int, array: list, cost: int):
        self._name = name
        self.k = k
        self.array = array
        self.cost = cost

    def __str__(self) -> str:
        return 'task3_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base1',
        k=2,
        array=[1, 2, 3, 4],
        cost=1,
    ),
    Case(
        name='base1',
        k=3,
        array=[1, 2, 3, 4],
        cost=2,
    ),
    Case(
        name='base1',
        k=3,
        array=[5, 3, 4, 2, 6],
        cost=2,
    ),
    Case(
        name='base1',
        k=4,
        array=[5, 3, 50, 2, 4, 5],
        cost=3,
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task3(case: Case) -> None:
    answer = task3(k=case.k, array=case.array)
    assert answer == case.cost
