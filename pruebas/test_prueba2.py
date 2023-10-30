
from prueba2 import comparacion
import pytest

def test_comparacion():
    assert comparacion(1, 1) == 0
    assert comparacion(1, 0) == 1
    assert comparacion(-100, 100) == 100