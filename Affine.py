from Oving3.Cipher import Cipher
from Oving3.cypto_util import modular_inverse
import random


class Affine(Cipher):

    def __init__(self):
        super().__init__()

    def encode(self, s, r, r2):
        encoded = ""
        for c in s:
            temp = ((ord(c) - 32) + r) % self.size
            numb = (temp * r2) % self.size
            encoded += self.alphabet[numb]
        return encoded

    def decode(self, s, r, r2):
        decoded = ""
        for c in s:
            key = modular_inverse(r2, len(self.alphabet))
            temp = ((ord(c) - 32) * key) % len(self.alphabet)
            numb = (temp - r) % self.size
            decoded += self.alphabet[numb]
        return decoded

    def generate_keys(self):
        keys = [random.randint(100, 1000), random.randint(100, 1000)]
        inv = modular_inverse(keys[1], self.size)
        while not inv:
            keys = [random.randint(100, 1000), random.randint(100, 1000)]
            inv = modular_inverse(keys[1], self.size)
        return keys
