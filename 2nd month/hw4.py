class vector:
    def __init__(self,x ,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"вектор: ({self.x};{self.y})"

    def __add__(self, other):
        return vector(self.x+other.x , self.y+other.y)


v1 = vector(2,3)
v2 = vector(3,5)

v3 = v1 + v2

print(v3)


class calculator:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"результат вычислении:{self.value}"

    def __add__(self, other):
        if isinstance(other,calculator):
            return calculator(self.value + other.value)
        return calculator(self.value + other)

    def __sub__(self, other):
        if isinstance(other,calculator):
            return calculator(self.value - other.value)
        return calculator(self.value - other)

    def __mul__(self, other):
        if isinstance(other,calculator):
            return calculator(self.value * other.value)
        return calculator(self.value * other)

    def __truediv__(self, other):
        val = other.value if isinstance(other, calculator) else other
        if val == 0:
            return "Ошибка: деление на ноль!"
        return calculator(self.value / val)


calc1 = calculator(15)
calc2 = calculator(4)
calc3 = calculator(0)

res_add = calc1 + calc2
print(res_add)

res_sub = calc1 - calc2
print(res_sub)

res_mul = calc1 * calc2
print(res_mul)

res_div = calc1 / calc2
print(res_div)

res_div1 = calc2 / calc3
print(res_div1)
