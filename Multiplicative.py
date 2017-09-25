from Oving3.Cipher import Cipher
from Oving3.cypto_util import modular_inverse
import random


class Multiplicative(Cipher):

    def __init__(self):
        super().__init__()

    #  TODO: VALIDATE THAT MODULO INVERSE EXIST

    def encode(self, s, r, r2):
        encoded = ""
        for c in s:
            numb = ((ord(c) - 32) * r) % self.size
            encoded += self.alphabet[numb]
        return encoded

    def decode(self, s, r, r2):
        decoded = ""
        for c in s:
            key = modular_inverse(r, len(self.alphabet))
            numb = ((ord(c) - 32) * key) % len(self.alphabet)
            decoded += self.alphabet[numb]
        return decoded

    def generate_keys(self):
        keys = [random.randint(100, 1000), random.randint(100, 1000)]
        inv = modular_inverse(keys[0], self.size)
        while not inv:
            keys = [random.randint(100, 1000), random.randint(100, 1000)]
            inv = modular_inverse(keys[0], self.size)
        return keys
