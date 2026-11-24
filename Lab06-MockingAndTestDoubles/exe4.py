# Student: Thet Htoo Naing
# Student ID: 6705140009

from unittest.mock import Mock
import pytest
def test_side_effect_list():
    mock = Mock()
    mock.get_data.side_effect = ["A", "B", "C"]

    assert mock.get_data() == "A"
    assert mock.get_data() == "B"
    assert mock.get_data() == "C"
    with pytest.raises(StopIteration):
        mock.get_data()
