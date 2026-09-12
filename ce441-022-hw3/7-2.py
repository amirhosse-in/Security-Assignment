block_size = 16

pad_size = 6
m = "1$ to original_destination"
m = m.encode() + pad_size.to_bytes(1, 'big') * pad_size
pad_size = 1
a = "99$ to attacker"
a = a.encode() + pad_size.to_bytes(1, 'big') * pad_size

c = bytes.fromhex("ad7fa3468caf0b5c01ec7be9b583fa350d2ce39b8cd57ee26270235cd6598592")
t = bytes.fromhex("905f6d5d03e5269a52aa3e33b558e764")

def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

c_prime = xor(xor(c[:block_size], m[:block_size]), a[:block_size])
t_prime = xor(c[block_size:2*block_size], m[block_size:2*block_size])

c_prime = hex(int.from_bytes(c_prime, 'big'))[2:]
t_prime = hex(int.from_bytes(t_prime, 'big'))[2:]

print(f"c', t' = ({c_prime}, {t_prime})")