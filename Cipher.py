import random


class Cipher(object):

    alphabet = ""
    size = None

    def __init__(self):
        for i in range(32, 127):
            self.alphabet += str(chr(i))
        self.size = 127 - 32

    # dummy method
    def encode(self, s, r, r2):
        pass

    # dummy method
    def decode(self, s, r, r2):
        pass

    def generate_keys(self):
        return [random.randint(100, 1000), random.randint(100, 1000)]

    # def verify(): ?


