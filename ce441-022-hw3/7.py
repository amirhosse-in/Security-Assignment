from Crypto.Cipher import AES
BLOCK_SIZE = 128 // 8

k = bytes.fromhex("875faffbaeea63eb878613b98460f4d2")

c1 = bytes.fromhex("d8b8239628a3f44c81e50cbd57aaac62586cdf1376c25fa8c23e8becf6be4688")
t1 = bytes.fromhex("abb859c60dd1450bd789a40bc3638f4e")

c2 = bytes.fromhex("dfb3319a23e6bf4d88b20cf342a9ac62447cc04770dd2cd2bc5b87e0fab24a84")
t2 = bytes.fromhex("b893a8d5032f5c004f11543626fc942e")

def dec_mac(k, c, t):
    m = AES.new(mode=AES.MODE_OFB, key=k, iv=k).decrypt(c)
    t_ = AES.new(mode=AES.MODE_CBC, key=k, iv=c[:BLOCK_SIZE]).encrypt(m)[-BLOCK_SIZE:]
    if t_ == t:
        return m
    else:
        return None


m1 = dec_mac(k, c1, t1)
m2 = dec_mac(k, c2, t2)

if m1 is not None:
    print(m1)
else:
    print("Invalid MAC for m1")

if m2 is not None:
    print(m2)
else:    
    print("Invalid MAC for m2")
