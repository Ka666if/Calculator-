class Calculator:
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            return "Ошибка: деление на ноль"
        return self.a / self.b


def show_results(calc, precision=None):
    if precision is None:
        print(f"Сложение: {calc.add()}")
        print(f"Вычитание: {calc.subtract()}")
        print(f"Умножение: {calc.multiply()}")
        print(f"Деление: {calc.divide()}")
    else:
        print(f"Сложение: {calc.add():.{precision}f}")
        print(f"Вычитание: {calc.subtract():.{precision}f}")
        print(f"Умножение: {calc.multiply():.{precision}f}")
        print(f"Деление: {calc.divide():.{precision}f}")


print("\n=== Примеры с целыми числами ===")
calc1 = Calculator(10, 2)
show_results(calc1)

print("\n=== Примеры с дробными числами ===")
calc2 = Calculator(10.5, 2.5)
show_results(calc2, precision=2)
