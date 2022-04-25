from main import *


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
