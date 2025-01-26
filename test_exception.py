import pytest


def test_passes():
    with pytest.raises(Exception) as e_info:
        x = 1 / 0