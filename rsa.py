from fractions import gcd
P = 19
Q = 113
N = P * Q
M = (P - 1) * (Q - 1)



def generate_e():
	e = 3
	while gcd(e,M) != 1:
		e += 2
	return e


def generate_d(e):
	d = 1
	while (e * d) % M != 1:
		d += 1
	return d


def char_to_ascii(text):
	num_arr = []
	for char in text:
		num_arr.append(ord(char))
	return num_arr




def encrypt(text, e):
	ascii_arr = char_to_ascii(text)
	enc_arr = []
	for num in ascii_arr:
		c = (num ** e) % N
		enc_arr.append(c)
	return enc_arr


def decrypt(enc_arr, d):
	dec_text = ''
	for num in enc_arr:
		ascii = (num ** d) % N
		dec_text += chr(ascii)
	return dec_text




def main():
	text = "ddwdwdw111!@$#"
	e = generate_e()
	d = generate_d(e)
	enc_text = encrypt(text, e)
	dec_text = decrypt(enc_text, d)
	print(text)
	print("enc_arr : ", enc_text)
	print("dec text: ", dec_text)


if __name__ == "__main__":
	main()
