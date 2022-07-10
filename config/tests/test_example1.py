import pytest


@pytest.mark.skip  # ten zostanie przeskoczony
def test_example():
    assert 1 == 1


@pytest.mark.xfail  # ten napewno obleje ale terminal zielony:)
def test_example2():
    assert 1 == 2


@pytest.mark.slow
def test_example3():
    assert 1 == 1


TEST_DIV_DATA = (
    (8, 2, 4),
    (0, 9, 0),
    (7, 2, 3.5)
)


def div(a, b):
    return a / b


@pytest.mark.parametrize("a,b, result", TEST_DIV_DATA)
def test_div(a, b, result):
    assert div(a, b) == result
