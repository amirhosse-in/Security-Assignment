from Crypto.Cipher import AES
from os import urandom # OS random generator

# 2-1
p = "2f20cb8872c99b696e6461cb906c202f"
c = "fd25a141381dbaef0fafc20ce028d934"

# brute force
for i in range(2**16):
    k = i.to_bytes(2, 'big') + b'\0' * 14
    E = AES.new(mode=AES.MODE_ECB, key=k).encrypt
    c_ = E(bytes.fromhex(p)).hex()
    if c_ == c:
        print(f"Key for 2-1 is: {k.hex()}")
        break


# 2-2
p = "2f20cb8872c99b696e6461cb906c202f"
c = "e4714ee833977599b7ec0a8d83a62164"

# brute force using MITM and hashtable
sub_ciphers = {}
for i in range(2**16):
    k1 = i.to_bytes(2, 'big') + b'\0' * 14
    E1 = AES.new(mode=AES.MODE_ECB, key=k1).encrypt
    sub_ciphers[E1(bytes.fromhex(p)).hex()] = k1
for i in range(2**16):
    k2 = i.to_bytes(2, 'big') + b'\0' * 14
    D2 = AES.new(mode=AES.MODE_ECB, key=k2).encrypt
    c_ = D2(bytes.fromhex(c)).hex()
    if c_ in sub_ciphers:
        print(f"Keys for 2-2 are: {sub_ciphers[c_].hex()} and {k2.hex()}")
        break

# 2-3
p = "2f20cb8872c99b696e6461cb906c202f"
c = "a6addbf32d0c6c5c87e311d3a35f78d3"

# brute force using MITM
sub_ciphers = {}
for i in range(2**16):
    k1 = i.to_bytes(2, 'big') + b'\0' * 14
    D1 = AES.new(mode=AES.MODE_ECB, key=k1).decrypt
    sub_ciphers[D1(D1(bytes.fromhex(p))).hex()] = k1
for i in range(2**16):
    k2 = i.to_bytes(2, 'big') + b'\0' * 14
    E2 = AES.new(mode=AES.MODE_ECB, key=k2).decrypt
    c_ = E2(bytes.fromhex(c)).hex()
    if c_ in sub_ciphers:
        print(f"Keys for 2-3 are: {sub_ciphers[c_].hex()} and {k2.hex()}")
        break