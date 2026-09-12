matrix = [[[] for j in range(32)] for i in range(32)]

for i in range(32):
	for j in range(32-i):
		matrix[j][i] = i+j
	for j in range(i):
		matrix[32-i+j][i] = j

persian = ["ا","ب","پ","ت","ث","ج","چ","ح","خ","د","ذ","ر","ز","ژ","س","ش","ص","ض","ط","ظ","ع","غ","ف","ق","ک","گ","ل","م","ن","و","ه","ی"]
cipher = [23, 28, 22, 11, 31, 22, 3, 22, 28, 31, 8, 7, 9, 0, 11, 12, 5, 3, 4, 8, 27, 19, 31, 23, 3, 22, 17, 1, 22, 11, 10, 27, 20, 14, 22, 26, 25, 9, 4, 13]
word = [1,0,11,0,28,1,30,0,11,31]
key_length = 9

def find(index, value):
	for i in range(32):
		if matrix[i][index] == value:
			return i

main_key = []
for i in range(len(cipher) - key_length):
	key = [-1 for j in range(9)]
	flag = 1
	for j in range(10):
		index = (i+j) % 9
		key_element = find(word[j], cipher[i+j])
		if key[index] == -1:
			key[index] = key_element
		elif key[index] != -1 and key[index] != key_element:
			flag = 0
			break
	if flag == 1:
		print(f"index: {i}")
		main_key = key
	
key = ""
for i in range(len(main_key)):
	key += persian[main_key[i]]
	

print(f"key is {key}")

def find(key_element, ciphered):
	for i in range(32):
		if matrix[key_element][i] == ciphered:
			return i

plain = []
for i in range(len(cipher)):
	plain.append(find(main_key[i%9], cipher[i]))

text = ""
for i in range(len(plain)):
	text += persian[plain[i]]

print(text)
