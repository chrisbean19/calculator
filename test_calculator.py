import calculator

def test_multiply_positive():
    assert calculator.multiply(3, 3) == 9, "Should be 9"

def test_multiply_negative():
    assert calculator.multiply(-3, -3) == 9, "Should be 9"

def test_multiply_mixed():
    assert calculator.multiply(-3, 3) == -9, "Should be -9"

def test_multiply_zero():
    assert calculator.multiply(3, 0) == 0, "Should be 0"

def test_add():
    assert calculator.add(3, 3) == 6, "Should be 6"

def test_add_to_zero():
    assert calculator.add(3, -3) == 0, "Should be 0"

def test_add_to_negative():
    assert calculator.add(3, -6) == -3, "Should be -3"

def test_subtract():
    assert calculator.subtract(3, 2) == 1, "Should be 1"

def test_subtract_to_zero():
    assert calculator.subtract(3, 3) == 0, "Should be 0"

def test_subtract_negative_to_positive():
    assert calculator.subtract(-3, -6) == 3, "Should be 3"

def test_divide():
    assert calculator.divide(9, 3) == 3, "Should be 3"

def test_divide_by_zero():
    assert calculator.divide(9, 0) == 9000, "Should be 9000"

def test_divide_negative():
    assert calculator.divide(9, -3) == -3, "Should be -3"

if __name__ == "__main__":
    test_multiply_positive()
    test_multiply_negative()
    test_multiply_mixed()
    test_multiply_zero()
    test_add()
    test_add_to_zero()
    test_add_to_negative()
    test_subtract()
    test_subtract_to_zero()
    test_subtract_negative_to_positive()
    test_divide()
    test_divide_by_zero()
    test_divide_negative()
    print("Everything passed")
