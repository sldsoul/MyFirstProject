def check(a, chislo):
    if a < chislo:
        return "меньше"
    elif a > chislo:
        return "больше"
    else:
        return "правильно"
def test_check():
    assert check(5,10) == "меньше"
    assert check(15,10) == "больше"
    assert check(7,7) == "правильно"
test_check()
print("тест прошел успешно")