import pytest

from .task import task4


class Case:
    def __init__(self, name: str, lamps: list, groups: list, answers: list):
        self._name = name
        self.lamps = lamps
        self.groups = groups
        self.answers = answers

    def __str__(self) -> str:
        return 'task4_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base1',
        lamps=[0, 0, 1, 1, 1, 0, 0],
        groups=[
            [1, 4, 6],
            [3, 4, 7],
            [2, 3]
        ],
        answers=[1, 2, 3, 3, 3, 3, 3],
    ),
    Case(
        name='base2',
        lamps=[0, 0, 1, 1, 0, 0, 1, 1],
        groups=[
            [1, 3, 8],
            [1, 2, 5, 6, 7],
            [6, 8],
            [3, 5],
            [4, 7],
            [2],
        ],
        answers=[1, 1, 1, 1, 1, 1, 4, 4],
    ),
    Case(
        name='base3',
        lamps=[1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0],
        groups=[
            [2, 3],
            [5, 6],
            [8, 9],
            [12, 13, 14, 15, 16],
            [19],
        ],
        answers=[0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5],
    ),
    Case(
        name='base4',
        lamps=[0, 1, 0],
        groups=[
            [1, 2],
            [2, 3],
            [1, 3]
        ],
        answers=[1, 1, 1]
    ),
    Case(
        name='base5',
        lamps=[1, 0, 0],
        groups=[
            [1, 2],
            [2, 3],
            [1, 3]
        ],
        answers=[0, 1, 1]
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task4(case: Case) -> None:
    answer = task4(lamps=case.lamps, groups=case.groups)
    assert answer == case.answers
