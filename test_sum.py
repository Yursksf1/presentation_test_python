def test_sum():
    assert sum([1, 2, 4]) == 6, "Should be 6"


def multiplicar(a, b):
    return a*b

def test_multiplicar():
    assert multiplicar(4, 4) == 16
    assert multiplicar(2, 5) == 11
    assert multiplicar(3, 5) == 15

if __name__ == "__main__":
    # test_sum()
    test_multiplicar()
    print("Everything passed")