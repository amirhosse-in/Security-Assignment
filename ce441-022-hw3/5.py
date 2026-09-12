p = 288918539521089348336793240678493497771
alpha = 3
alpha_x1 = 12782377710547948619020211758683185425 % p
alpha_x2 = 183364455173249021598006044125891817111 % p

def custom_pow(base, exp, mod):
    if exp == 0:
        return 1
    if exp == 1:
        return base % mod
    if exp % 2 == 0:
        return custom_pow(base, exp//2, mod)**2 % mod
    else:
        return (base * custom_pow(base, exp-1, mod)) % mod

x1 = -1
x2 = -1
range_start = 2
while True:
    flag = 1
    for i in range(range_start, 2*range_start):
        if custom_pow(alpha, i, p) == alpha_x1:
            print(f"x1 is {i}")
            x1 = i
            flag = 0
            break
    for i in range(range_start, 2*range_start):
        if custom_pow(alpha, i, p) == alpha_x2:
            print(f"x2 is {i}")
            x2 = i
            flag = 0
            break
    if flag == 0:
        break
    range_start *= 2

if x1 == -1:
    print(f"common key is (alpha^x_1)^x_2 = {custom_pow(alpha_x1, x2, p)}")
else:
    print(f"common key is (alpha^x_2)^x_1 = {custom_pow(alpha_x2, x1, p)}")