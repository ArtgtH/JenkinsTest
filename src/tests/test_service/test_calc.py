from service.calc import increment


def test_calc():
    res = increment()

    assert res == 10
