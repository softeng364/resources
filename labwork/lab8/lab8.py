# -*- coding: utf-8 -*-
#
# lab8.py: This is a complete version 
# of the code snippets in lab8.md
#
from sympy.ntheory import totient
from sympy.ntheory.factor_ import primefactors

import math  # for math.gcd

p = 5                # "prime p"
q = 7                # "prime q"
n = p*q              # modulus
z = (p - 1)*(q - 1)  # Euler totient
e = 5                # encryption/public exponent
assert math.gcd(e, z) == 1
d = 29               # decryption/private exponent
assert (e*d - 1) % z == 0

m = 12               # plaintext
c = pow(m, e, n)     # ciphertext
assert c is 17

m_new = pow(c, d, n) # plaintext?...
assert m == m_new    # ... yes!

assert z == totient(p)*totient(q) == totient(n)

# ============================================================================
# RSA with more realistic data
# ============================================================================

#
# RSA prime factors
#
num_bits = 1024
lower = 1 << (num_bits - 1)
upper = (1 << num_bits) - 1

assert lower.bit_length() == upper.bit_length() == num_bits
assert (lower - 1).bit_length() == num_bits - 1
assert (upper + 1).bit_length() == num_bits + 1

#
# RSA encryption/public factor
#
from sympy.ntheory.generate import randprime
p = randprime(lower, upper)
q = randprime(lower, upper)

from sympy.ntheory.primetest import isprime
assert isprime(p)
assert isprime(q)
assert p.bit_length() == num_bits
assert q.bit_length() == num_bits

n = p*q
z = (p - 1)*(q - 1)

e = 65537  # specified encryption exponent
import math
assert math.gcd(e, z) == 1

#
# RSA decryption/private factor
#
from sympy.core.numbers import mod_inverse
d = mod_inverse(e, z)
assert (e*d - 1) % z == 0

#
# Extracting the integer underlying an arbitrary string
#
import sys
# Using p, q, n, z as before
m_str = 'Tøp Secrèt!'
m_bytes = m_str.encode()
m = int.from_bytes(m_bytes, byteorder=sys.byteorder, signed=False)
assert m < n, 'Modulus is too small for message'

#
# RSA encryption and decryption
#
c = pow(m, e, n)  # ciphertext
envelope = (c, len(m_bytes))  # "pack"
# Transmit ciphertext over insecure channel...
c_received, length = envelope  # "unpack"
m_new = pow(c_received, d, n)
m_bytes_new = m_new.to_bytes(length, byteorder=sys.byteorder, signed=False)
m_str_new = m_bytes_new.decode()
print(m_str_new)
assert m_str_new == m_str
