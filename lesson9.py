# ООП обьектно ориентированное Программирование

# human = ["Mark", 20, "osh"]
# переменная = ее значения обозначеные одним из восьми типов данных
# Класс это чертеж чего либо; чертеж это макет то есть его нельзя напрямую использовать
# обьект (экземпляр) - это полноценная сделанная по чертежу вещь

class cat:
    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color

    def say_meow(self):
        print(f"{self.name} мяу мяу")

cat1 = cat(name = "broski",color = "blood sky")
print(cat1.name, cat1.color)
cat1.say.meow()


cat2 = cat(name = "broski.bro",color = "nigga")
print(cat2.name, cat2.color)
cat2.say.meow()


class piggybank:
    def __init__(self, owner):
        self.owner = owner
        self.coins = 0

    def add_money(self, amount: int):
        if amount > 0:
            self.coins += amount
            print(f"В вашу копилку добавлено {amount} долларов. дорогой/ая {self.owner}. ваш баланс {self.coins} долларов")
        else:
            print(f"Введите сумму монет числами уважаемый в виде (1, 2, 3, 4, 5, 6, 7, 8, 9 и тд)")

    def break_piggy(self) -> int:
        saved = self.coins
        self.coins = 0
        print(f"ты ебень зачем ты разбил копилку свою {self.owner}, всего там было долларов {saved}")
        return saved


mr_piggy = piggybank("Mark")
mr_piggy.add_money(100)
mr_piggy.add_money(500)
mr_piggy.add_money(10000)


money = mr_piggy.break_piggy()
print(f"у тебя на руках есть {money} долларов")
print(f"Остаток в копилке {mr_piggy.coins} долларов")