from Oving3.Cipher import Cipher


class Caesar(Cipher):

    def __init__(self):
        super().__init__()

    def encode(self, s, r, r2):
        encoded = ""
        for c in s:
            numb = ((ord(c) - 32) + r) % self.size
            encoded += self.alphabet[numb]
        return encoded

    def decode(self, s, r, r2):
        decoded = ""
        for c in s:
            numb = ((ord(c) - 32) - r) % self.size
            decoded += self.alphabet[numb]
        return decoded
