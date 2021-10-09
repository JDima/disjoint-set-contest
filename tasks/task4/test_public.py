import pytest

from .task import task4


class Case:
    def __init__(self, name: str, switches: list, groups: list, answers: list):
        self._name = name
        self.switches = switches
        self.groups = groups
        self.answers = answers

    def __str__(self) -> str:
        return 'task4_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base1',
        switches=[0, 0, 1, 1, 1, 0, 0],
        groups=[
            [1, 4, 6],
            [3, 4, 7],
            [2, 3]
        ],
        answers=[1, 2, 3, 3, 3, 3, 3],
    ),
    Case(
        name='base2',
        switches=[0, 0, 1, 1, 0, 0, 1, 1],
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
        switches=[1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0],
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
        switches=[0, 1, 0],
        groups=[
            [1, 2],
            [2, 3],
            [1, 3]
        ],
        answers=[1, 1, 1]
    ),
    Case(
        name='base5',
        switches=[1, 0, 0],
        groups=[
            [1, 2],
            [2, 3],
            [1, 3]
        ],
        answers=[0, 1, 1]
    ),
    Case(
        name='base6',
        switches=[0, 0, 0, 1, 1],
        groups=[
            [1, 2, 3],
            [4],
            [3, 4, 5]
        ],
        answers=[1, 1, 1, 1, 1]
    )
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task4(case: Case) -> None:
    answer = task4(switches=case.switches, groups=case.groups)
    assert answer == case.answers
