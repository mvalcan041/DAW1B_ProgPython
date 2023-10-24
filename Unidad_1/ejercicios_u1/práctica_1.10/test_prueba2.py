
from prueba2 import comparacion
import pytest

def test_comparacion():
    assert comparacion(1, 1) == 0
    assert comparacion(0, 1) == 1
    assert comparacion(100, -100) == 100

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
      (1, 1, 0),
      (1, 0, 1),
      (100, -100, 100),
      (-15, -1, -1),
      (-3, 8, 8),
      (9, 354, 354)
    ]
  )
def test_comparacion_params(input_n1, input_n2, expected):
    assert comparacion(input_n1, input_n2) == expected
