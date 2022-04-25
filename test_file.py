from main import *
import pytest


def test_parse_commands():
    assert parse_co() == [{'function': 'parse', 'help': 'file help', 'value': 'file'}]


def test_copy_commands():
    assert copy_co() == [{'function': 'copy', 'help': 'copy help', 'value': 'file'}]


def test_functional_commands():
    assert functional_co() == [{'function': 'parse', 'help': 'file help', 'value': 'file', '_list': 'parse', '_counter': 1},
                               {'function': 'copy', 'help': 'copy help', 'value': 'file', '_list': 'copy', '_counter': 1}]


def test_random_length():
    assert len(random_co()) == 2


def test_bad_length():
    assert len(bad_co()) == 3


# parametrize function example see below------------------------

# pytest fixtures
@pytest.fixture()
def file_data():
    with open('data.txt', 'r') as file:
        data = json.loads(file.read())
    return data


def parse_co(file_data):
    parse_c = []
    for row in file_data:
        if 'function' in row and row['function'] == 'parse':
            parse_c.append(row.copy())
    return parse_c


# parameterize test cases
@pytest.mark.parametrize("compare_with", [{'function': 'parse', 'help': 'file help', 'value': 'file'}])
def test_parse_command_test(file_data, compare_with):
    assert parse_co(file_data) == [compare_with]