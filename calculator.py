class MathBox:
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)

    def plus(self):
        return self.a + self.b

    def minus(self):
        return self.a - self.b

    def times(self):
        return self.a * self.b

    def divided_by(self):
        if self.b == 0:
            return "Ошибка: деление на ноль"
        return self.a / self.b


def show_results(calc, precision=None):
    if precision is None:
        print(f"Сложение: {calc.plus()}")
        print(f"Вычитание: {calc.minus()}")
        print(f"Умножение: {calc.times()}")
        print(f"Деление: {calc.divided_by()}")
    else:
        print(f"Сложение: {calc.plus():.{precision}f}")
        print(f"Вычитание: {calc.minus():.{precision}f}")
        print(f"Умножение: {calc.times():.{precision}f}")
        print(f"Деление: {calc.divided_by():.{precision}f}")


print("\n=== Примеры с целыми числами ===")
box1 = MathBox(10, 2)
show_results(box1)

print("\n=== Примеры с дробными числами ===")
box2 = MathBox(10.5, 2.5)
show_results(box2, precision=2)
