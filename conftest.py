import pytest

from main import Voting


@pytest.fixture
def options():
    return ["Да", "Нет", "Может быть"]


@pytest.fixture
def voting(options):
    return Voting(options)


@pytest.fixture
def voted_voting(voting):
    voting.vote(1)
    voting.vote(1)
    voting.vote(2)
    return voting

