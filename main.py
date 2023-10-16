class   Cards:

    def __init__(self, number) -> None:
        self.number = number
        self.numbers = {}
        self.remaining = 15
        pass

    def isFull(self) -> bool:
        if self.remaining == 0:
            return True
        return False

    def asNum(self, number) -> bool:
        if number in self.numbers:
            return True
        return False

    def markNum(self, number) -> None:
        self.numbers[number] = 1
        self.remaining -= 1

class   Player:

    def __init__(self, name) -> None:
        self.name = name
        self.cards = []
        pass
