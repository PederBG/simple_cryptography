from Oving3.Sender import Sender
from Oving3.Receiver import Receiver
from Oving3.Hacker import Hacker
from Oving3.Caesar import Caesar
from Oving3.Multiplicative import Multiplicative
from Oving3.Affine import Affine
from Oving3.Unbreakable import Unbreakable
from Oving3.RSA import RSA


class Chat:

    s = None
    r = None

    def __init__(self, s, r):
        if type(s) != Sender or type(r) != Receiver:
            raise ValueError("Invalid arguments!")
        self.s = s
        self.r = r

    def set_key(self, key, key2=3):
        self.s.set_key(key, key2)
        self.r.set_key(key, key2)

    def set_random_key(self):
        if isinstance(self.r.cipher, RSA):
            keys = self.r.cipher.generate_keys()
            self.r.set_key(keys[0][1], keys[0][0])
            self.s.set_key(keys[1][1], keys[1][0])
            print("Generated public key (n, p): (" + str(keys[1][0]) + ", " + str(keys[1][1]) + ")")
        else:
            keys = self.s.cipher.generate_keys()
            self.set_key(keys[0], keys[1])
            if isinstance(self.r.cipher, Affine):
                print("Generated keys:", keys[0], keys[1])
            else:
                print("Generated key:", keys[0])

    def send_message(self, message):
        encoded = self.s.operate_cipher(message)
        print("Encoded message:", encoded)
        print("...")
        decoded = self.r.operate_cipher(encoded)
        print("Decoded back:", decoded)
        return encoded
# -----------------------------------------------------------------------------------------


def run():
    while True:
        cip = input("Choose a cipher: -> Caesar: 1 -> Multiplicative: 2 -> Affine: 3 -> Unbreakable: 4 -> RSA: 5\n")

        if cip == "EXIT":
            quit()

        hacker = False
        if cip != str(5):
            if input("Create hacker? y/n") == "y":
                hacker = True
            else:
                hacker = False

        try:
            cip = int(cip)
            if cip not in range(1, 6):
                run()
        except ValueError:
            run()
        ciphers = [None, Caesar(), Multiplicative(), Affine(), Unbreakable(), RSA()]

        c = Chat(Sender(ciphers[cip]), Receiver(ciphers[cip]))
        print("Creating random key(s)...")
        c.set_random_key()

        mes = input("Send message: \n")
        print()
        encoded = c.send_message(mes)
        print("----------------------------------------------")
        if hacker:
            print("Hacking the code...")
            print("Using the decrypted message:", encoded)
            h = Hacker(ciphers[cip])
            hacked_result = h.hack(encoded)
            print("...")
            print("Sent message: " + str(hacked_result[0]) + "\nKey used: " + str(hacked_result[2]) +
                  " (modulo " + str(h.cipher.size) + ")")
            print()
            print("Running again, write EXIT to quit.")
run()
