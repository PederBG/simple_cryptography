from Oving3.Person import Person
from Oving3.Caesar import Caesar
from Oving3.Multiplicative import Multiplicative
from Oving3.Affine import Affine
from Oving3.Unbreakable import Unbreakable

class Hacker(Person):

    words = []
    limit = None

    def __init__(self, cip):
        super().__init__(cip, None, None)
        word_list = open("words.txt", "r")
        word = word_list.readline()
        while word:
            self.words.append(word.split("\n")[0])
            word = word_list.readline()
        word_list.close()

        self.limit = self.cipher.size

    def operate_cipher(self, s):
        pass

    def hack(self, s):
        best_match = [None, 0, None, None]

        if isinstance(self.cipher, Affine):

            for i in range(0, self.limit):
                for j in range(0, self.limit):
                    decode = self.cipher.decode(s, i, j)
                    decoded_words = decode.split(" ")
                    match = 0
                    for word in decoded_words:
                        if word in self.words and len(word) > 0:
                            match += 1
                    if match > best_match[1]:
                        best_match = (decode, match, i, j)
                    if best_match[1] == len(decoded_words):  # hvis oversettelsen er perfekt
                        return best_match
            return best_match

        elif isinstance(self.cipher, Unbreakable):
            for i in self.words:
                print(i)
                decode = self.cipher.decode(s, i, 0)
                decoded_words = decode.split(" ")
                match = 0
                for word in decoded_words:
                    if word in self.words and len(word) > 0:
                        match += 1
                if match > best_match[1]:
                    best_match = (decode, match, i)
                    print(best_match)
                if best_match[1] == len(decoded_words):  # hvis oversettelsen er perfekt
                    return best_match
            return best_match

        else:
            for i in range(0, self.limit):  # Denne bruker laaaaang tid
                decode = self.cipher.decode(s, i, 0)
                decoded_words = decode.split(" ")
                match = 0
                for word in decoded_words:
                    if word in self.words and len(word) > 0:
                        match += 1
                if match > best_match[1]:
                    best_match = (decode, match, i)
                if best_match[1] == len(decoded_words):  # hvis oversettelsen er perfekt
                    return best_match
            return best_match
