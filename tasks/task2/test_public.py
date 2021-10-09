import pytest

from .task import task2


class Case:
    def __init__(self, name: str, childs: list, powers: list):
        self._name = name
        self.childs = childs
        self.powers = powers

    def __str__(self) -> str:
        return 'task2_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base1',
        childs=[1, 2, 3, 4, 5, 4, 3, 2, 1, 6],
        powers=[6, 4, 4, 3, 3, 2, 2, 1, 1, 1],
    ),
    Case(
        name='base2',
        childs=[1, 2, 3],
        powers=[3, 2, 1],
    ),
    Case(
        name='base3',
        childs=[7, 9, 13, 6],
        powers=[13, 9, 7, 6],
    ),
    Case(
        name='base4',
        childs=[1, 3, 5, 2, 4],
        powers=[5, 3, 2, 2, 1]
    ),
    Case(
        name='base5',
        childs=[3, 2, 8, 4, 5, 4, 3, 5, 1, 1, 9],
        powers=[9, 4, 4, 4, 3, 3, 2, 2, 1, 1, 1],
    ),
    Case(
        name='base6',
        childs=[5],
        powers=[5]
    ),
    Case(
        name='base7',
        childs=[3, 2, 8, 4, 5, 4, 7, 9, 13, 6, 3, 5, 1, 1, 9, 1, 2, 3, 4, 5, 4, 3, 2, 1, 6, 20],
        powers=[20, 9, 7, 6, 4, 4, 4, 4, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    )
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task2(case: Case) -> None:
    answer = task2(childs=case.childs)
    assert answer == case.powers
