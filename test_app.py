from app import sumar, restar, multiplicar, dividir

def test_sumar():
    assert sumar(5, 3) == 10

def test_restar():
    assert restar(10, 4) == 6

def test_multiplicar():
    assert multiplicar(4, 3) == 12

def test_dividir():
    assert dividir(10, 2) == 5