import random

class Dice():

    def __init__(self, sides) -> None:
        self.sides = sides

    def __call__(self) -> int:
        return self.roll()

    def __str__(self) -> str:
        return f"A {self.sides} sided die."

    def roll(self) -> int:
        return random.randint(1, self.sides)

class DiceBag():

    def __init__(self, *args) -> None:
        self.bag = []
        for item in args:
            self.bag.append(Dice(item))

    def __call__(self) -> list[int]:
        return self.roll()

    def __str__(self) -> str:
        result = "A dice bag containing:"
        for dice in self:
            result += "\n"
            result += "  " + str(dice)
        return result

    def __iter__(self):
        return (dice for dice in self.bag)

    def roll(self, filter=None) -> list[int]:
        if filter:
            return [dice() for dice in self if dice.sides == filter]
        return [dice() for dice in self.bag]

    def total(self, filter=None) -> int:
        return sum(self.roll(filter=filter))

    def max(self, filter=None) -> int:
        return max(self.roll(filter=filter))

    def min(self, filter=None) -> int:
        return min(self.roll(filter=filter))

if __name__=='__main__':
    my_dice = Dice(6)
    print(my_dice)
    print(my_dice())
    my_bag = DiceBag(*range(1,10))
    print(my_bag)
    print(my_bag())
    print(my_bag.roll(filter=5))
    twenties = DiceBag(20, 20, 20)
    print(twenties)
    print(twenties())
