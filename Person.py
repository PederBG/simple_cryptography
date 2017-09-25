class Person(object):

    cipher = None
    key = None  # is e/d value for RSA
    key2 = None  # is n value for RSA

    def __init__(self, cip, key=3, key2=3):
        self.cipher = cip
        self.key = key
        self.key2 = key2

    def set_key(self, key, key2=3):
        self.key = key
        self.key2 = key2

    def get_key(self):
        return [self.key, self.key2]

    # dummy method
    def operate_cipher(self, s):
        pass
