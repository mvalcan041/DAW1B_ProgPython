
# Pytest "Ejercicio 2.1.1"

from src.e2_1_1 import edad
import pytest

def test_comparacion():
    assert edad(18) == True
    assert edad(2) == False
    assert edad(72) == True

@pytest.mark.parametrize(
    "input_n1, expected",
    [
      (1, False),
      (-1, False),
      (100, True),
      (14, False),
      (54, True),
      (9, False)
    ]
  )
def test_edad_params(input_n1, expected):
    assert edad(input_n1) == expected
