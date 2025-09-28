import pytest


class TestAbs:
    def test_abs1(self):
        assert 42 == abs(42), "Should be absolute value of a number"

    def test_abs2(self):
        assert -42 == abs(-42), "Should be absolute value of a number"


if __name__ == "__main__":
    pytest.main()
