import pytest
from principal import soma

def test_soma():
    assert soma(3,5)==8
    assert soma(8,4)==4
    assert soma(0,5)==5