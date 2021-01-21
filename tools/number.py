class Number:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def gen_numbers(self):
        numbers = [number for number in list(range(self.start, self.end + 1))]
        return numbers
