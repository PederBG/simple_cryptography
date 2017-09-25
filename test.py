from Oving3.Sender import Sender
from Oving3.Caesar import Caesar
from Oving3.Cipher import Cipher
from Oving3.Receiver import Receiver
from Oving3.cypto_util import *
import random

ss = Sender(Caesar())
rr = Receiver(Caesar())


a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
"""
p = generate_random_prime(5)
q = generate_random_prime(5)
print(p, q)

n = p * q
phi = (p - 1) * (q - 1)
print(n)
e = random.randint(3, phi-1)
print("e:", e)
d = modular_inverse(e, phi)
print("d:", d)
print("----------------")
enc = 100**e % n
print("Enc:", enc)

dec = enc**d % n
print(dec)

p1 = 53
p2 = 59
n = p1*p2
phi = (p1-1)*(p2-1)
e = 3
d = (2*phi + 1) // e
d2 = modular_inverse(e, phi)

print(n, phi, e, d, d2)
c = 89**e % n
print(c)

print(c**d % n)

"""
