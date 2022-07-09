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
