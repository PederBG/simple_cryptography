from Oving3.Person import Person


class Receiver(Person):

    def __init__(self, cip):
        super().__init__(cip)

    def operate_cipher(self, s):
        return self.cipher.decode(s, self.key, self.key2)

