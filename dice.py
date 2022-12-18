import random
from typing import Any

class Dice():
    """A dice object that can be rolled to return a random value.
    """

    def __init__(self, sides):
        """Construct dice instance.
        Dice are rolled to return a value between one and sides.
        Dice must have at least two sides to be rollable.

        Args:
            sides (_type_): Number of sides on the created dice.
        """
        self.sides = max(2, sides)

    def __call__(self) -> int:
        """Roll Dice by calling it directly.

        Returns:
            int: Rolled value
        """
        return self.roll()

    def __str__(self) -> str:
        """String representation of Dice.

        Returns:
            str: Descriptive string
        """
        return f"A {self.sides} sided die."

    def roll(self) -> int:
        """Roll the dice.

        Returns:
            int: Roll result
        """
        return random.randint(1, self.sides)

class DiceBag():
    """A collection of Dice that can be rolled together.
    """

    def __init__(self, *args) -> None:
        """Construct a group of dice that can be rolled together.

        Args:
            args (int): Each arg is a dice of the given sidedness.
        """
        ints = [int(arg) for arg in args]
        self.bag = []
        for num in ints:
            self.bag.append(Dice(num))

    def __call__(self, detailed=False) -> Any:
        """Roll DiceBag by calling it directly.

        Args:
            detailed (bool, optional): Whether or not to return results grouped by dice. Defaults to False.

        Returns:
            Any: Default roll returns a single list. Detailed roll returns a dictionary of lists.
        """
        if detailed:
            return self.detailed_roll()
        return self.roll()

    def __str__(self) -> str:
        """String representation of DiceBag.

        Returns:
            str: Descriptive string
        """
        result = f"A {len(self)} dice bag containing:"
        for dice in self:
            result += "\n  " + str(dice)
        return result

    def __len__(self) -> int:
        """Length of DiceBag.

        Returns:
            int: Number of dice in bag.
        """
        return len(self.bag)

    def __iter__(self):
        """Iterate over dice in bag.

        Returns:
            generator: Stored Dice objects.
        """
        return (dice for dice in self.bag)

    def roll(self, filter:int=None) -> list[int]:
        """Roll the entire bag of dice.

        Args:
            filter (int, optional): Roll only dice of the specified type. Defaults to None.

        Returns:
            list[int]: Roll results
        """
        if filter:
            return [dice() for dice in self if dice.sides == filter]
        return [dice() for dice in self.bag]

    def detailed_roll(self) -> dict:
        """Roll the entire bag of dice.

        Returns:
            dict: Roll results by dice size.
        """
        result = {}
        for dice in self:
            if dice.sides in result:
                result[dice.sides].append(dice())
            else:
                result[dice.sides] = [dice()]
        return result

    def pop(self) -> int:
        """Roll the last dice and remove it from the bag

        Returns:
            int: Result of rolling the removed dice.
        """
        result = self.bag[-1]()
        del self.bag[-1]
        return result

    def total(self, filter:int=None) -> int:
        """Roll the entire bag of dice and find the total.

        Args:
            filter (int, optional): Roll only dice of the specified type. Defaults to None.

        Returns:
            int: Sum of all rolled dice.
        """
        return sum(self.roll(filter=filter))

    def max(self, filter:int=None) -> int:
        """Roll the entire bag of dice and find the highest value.

        Args:
            filter (int, optional): Roll only dice of the specified type. Defaults to None.

        Returns:
            int: Largest roll result.
        """
        return max(self.roll(filter=filter))

    def min(self, filter:int=None) -> int:
        """Roll the entire bag of dice and find the smallest value.

        Args:
            filter (int, optional): Roll only dice of the specified type. Defaults to None.

        Returns:
            int: Smalled roll result.
        """
        return min(self.roll(filter=filter))

    def sub_total(self) -> dict:
        """Roll the entire bag of dice and find the subtotal by size.

        Returns:
            dict: Dice sizes and their subtotals
        """
        rolled = self.detailed_roll()
        for item in rolled:
            rolled[item] = sum(rolled[item])
        return rolled

    def sub_max(self) -> dict:
        """Roll the entire bag of dice and find the max by size.

        Returns:
            dict: Dice sizes and their largest rolled value.
        """
        rolled = self.detailed_roll()
        for item in rolled:
            rolled[item] = max(rolled[item])
        return rolled

    def sub_min(self) -> dict:
        """Roll the entire bag of dice and find the min by size.

        Returns:
            dict: Dice sizes and their smallest rolled value.
        """
        rolled = self.detailed_roll()
        for item in rolled:
            rolled[item] = min(rolled[item])
        return rolled


if __name__=='__main__':
    my_dice = Dice(6)
    print(my_dice)
    print(my_dice())
    my_bag = DiceBag(6,6,6,4,4,4,10,10,10)
    print(my_bag)
    print(my_bag())
    print(my_bag.roll(filter=5))
    print(my_bag.detailed_roll())
    twenties = DiceBag(20, 20, 20)
    print(twenties)
    print(twenties())
    print(twenties.detailed_roll())
    print(twenties.sub_total())
    print(twenties.sub_max())
    print(twenties.sub_min())
    print(twenties.pop())
    print(twenties.detailed_roll())
