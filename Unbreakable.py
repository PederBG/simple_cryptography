from Oving3.Cipher import Cipher
import random


class Unbreakable(Cipher):

    def __init__(self):
        super().__init__()

    def encode(self, s, r, r2):
        encoded = ""
        i = 0
        while True:  # filling in word again if message is longer than word
            if len(r) >= len(s):
                break
            if i == len(r):
                i = 0
            r += r[i]
            i += 1
        for c in range(0, len(s)):
            numb = ((ord(s[c]) - 32) + (ord(r[c]) - 32)) % self.size
            encoded += self.alphabet[numb]
        return encoded

    def decode(self, s, r, r2):
        decoded = ""
        i = 0
        while True:
            if len(r) >= len(s):
                break
            if i == len(r):
                i = 0
            r += r[i]
            i += 1
        for c in range(0, len(s)):
            numb = ((ord(s[c]) - 32) + (len(self.alphabet) - (ord(r[c]) - 32))) % self.size
            decoded += self.alphabet[numb]
        return decoded

    def generate_keys(self):
        word_list = open("words.txt", "r")
        word = word_list.readline()

        legal_words = []
        while word:
            legal_words.append(word.split("\n")[0])
            word = word_list.readline()
        word_list.close()
        return [legal_words[random.randint(0, int(len(legal_words) / 100))], 0]
