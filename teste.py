import pytest
from principal import soma

def test_soma():
    assert soma(3,5)==8
    assert soma(2,4)==6
    assert soma(1,3)==4