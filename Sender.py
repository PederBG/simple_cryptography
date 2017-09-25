from Oving3.Person import Person


class Sender(Person):

    def __init__(self, cip):
        super().__init__(cip)

    def operate_cipher(self, s):
        return self.cipher.encode(s, self.key, self.key2)
