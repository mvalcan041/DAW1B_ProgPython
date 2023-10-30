
# Pytest "Ejercicio 2.1.2"

from src.e2_1_2 import pswdTrue
import pytest

def test_pswdTrue():
    assert pswdTrue("ConTRaSEña") == True
    assert pswdTrue("c0ntraseña") == False
    assert pswdTrue("contraseña") == True
    assert pswdTrue("CONTRASEÑA") == True
    assert pswdTrue("manzana") == False

@pytest.mark.parametrize(
    "input_n1, expected",
    [
      ("contraseÑA", True),
      ("contrasena", False),
      ("CONTRASEÑA", True),
      ("platano", False),
      ("contraseña", True),
      ("fsdafgbasd", False)
    ]
  )
def test_pswdTrue_params(input_n1, expected):
    assert pswdTrue(input_n1) == expected
