import pytest

from .task import task2


class Case:
    def __init__(self, name: str, pandas: list, powers: list):
        self._name = name
        self.pandas = pandas
        self.powers = powers

    def __str__(self) -> str:
        return 'task2_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base',
        pandas=[1, 2, 3, 4, 5, 4, 3, 2, 1, 6],
        powers=[6, 4, 4, 3, 3, 2, 2, 1, 1, 1],
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task2(case: Case) -> None:
    answer = task2(pandas=case.pandas)
    assert answer == case.powers
