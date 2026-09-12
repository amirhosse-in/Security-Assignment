n1 = 882389665577830838482125131852013816279695311
n2 = 726247788835915752041026275800104626981008161

e1 = 65537
e2 = 5

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

common_p = gcd(n1, n2)
q1 = n1 // common_p
q2 = n2 // common_p
print(f"common_p: {common_p}, q1: {q1}, q2: {q2}")

phi = (common_p - 1) * (q1 - 1)
d1 = pow(e1, -1, phi)
phi = (common_p - 1) * (q2 - 1)
d2 = pow(e2, -1, phi)

print(f"private1: ({n1}, {d1})\nprivate2: ({n2}, {d2})")
