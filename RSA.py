from Oving3.Cipher import Cipher
from Oving3.cypto_util import *
import random


class RSA(Cipher):

    prime_bits = 10

    def __init__(self):
        super().__init__()

    def encode(self, s, e, n):
        t = blocks_from_text(s, 2)  # deler meldingen s opp i blokker av bits representert ved int
        for elem in t:              # krypterer hver int blokk
            elem = pow(elem, e, n)

        return t

    def decode(self, c, d, n):
        for elem in c:
            elem = pow(elem, d, n)

        decoded = text_from_blocks(c, self.prime_bits)
        return decoded

    def generate_keys(self):
        p = generate_random_prime(self.prime_bits)
        q = generate_random_prime(self.prime_bits)
        while p == q:
            p = generate_random_prime(self.prime_bits)
            q = generate_random_prime(self.prime_bits)
        n = p * q
        phi = (p - 1) * (q - 1)
        e = random.randint(3, phi - 1)
        d = modular_inverse(e, phi)
        while not d:
            e = random.randint(3, phi - 1)
            d = modular_inverse(e, phi)
        return [(n, d), (n, e)]
