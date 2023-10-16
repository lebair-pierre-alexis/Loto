class   Card:

    def __init__(self, number) -> None:
        self.number = number
        self.numbers = {}
        self.remaining = 0
        pass

    def isFull(self) -> bool:
        if self.remaining == 0:
            return True
        return False

    def isEmpty(self) -> bool:
        if self.remaining == 15:
            return True
        return False

    def asNum(self, number) -> bool:
        if number in self.numbers.keys():
            return True
        return False

    def markNum(self, number) -> None:
        self.numbers[number] = 1
        self.remaining -= 1

    def resetMark(self) -> None:
        for i in self.numbers.keys():
            self.numbers[i] = 0

    def missingNumbers(self) -> list[int]:
        missing = []
        for number in self.numbers:
            if self.numbers[number] == 0:
                missing.append(number)
        return missing
