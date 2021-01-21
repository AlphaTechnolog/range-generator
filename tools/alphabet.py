class Alphabet:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def gen_alphabet(self):
        generated = [chr(i) for i in range(ord(self.start), ord(self.end) + 1)]
        return generated
