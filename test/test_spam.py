import pytest

@pytest.mark.parametrize(
    "spam",
    list(range(1, 1000))
)
def test_spam(spam):
    assert False