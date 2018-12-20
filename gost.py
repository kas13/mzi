"""encryption standard GOST 28147-89"""


S = [
    [4,10,9,2,13,8,0,14,6,11,1,12,7,15,5,3],
    [14,11,4,12,6,13,15,10,2,3,8,1,0,7,5,9],
    [5,8,1,13,10,3,4,2,14,15,12,7,6,0,9,11],
    [7,13,10,1,0,8,9,15,14,4,6,12,11,2,5,3],
    [6,12,7,1,5,15,13,8,4,10,9,14,0,3,11,2],
    [4,11,10,0,7,2,1,13,3,6,8,5,9,12,15,14],
    [13,11,4,1,3,15,5,9,0,10,14,7,6,8,2,12],
    [1,15,13,0,5,7,10,4,9,2,3,14,6,11,8,12]
]

K = [0,1,2,3,4,5,6,7,0,1,2,3,4,5,6,7,0,1,2,3,4,5,6,7,7,6,5,4,3,2,1,0]
MOD = 4294967296
ALL_KEYS = []


def make_all_keys(key):
	""" From the 256 bits key make 8 keys of 32 bits """

	if len(key) != 32:
		raise Exception("The key must be 32 bytes")

	bits_ar = chars_to_bits(key)
	for i in range(0, len(bits_ar), 32):
		value = "".join([str(bit) for bit in bits_ar[i:i+32]])
		ALL_KEYS.append(int(value, 2))


def chars_to_bits(text):
	"""	From the text make bit string	"""

	bits_str = ''
	for char in text:
		bits = bin(ord(char))[2:]
		while len(bits) < 8:
			bits = "0" + bits
		bits_str += bits
	return bits_str


def bits_to_chars(bits_arr):
	""" From the bits array make text """

	chars_arr = []
	for i in range(0, len(bits_arr), 8):
		byte = bits_arr[i:i+8]
		char = "".join([str(bit) for bit in byte])
		chars_arr.append(chr(int(char, 2)))
	return "".join(chars_arr)


def split_s(number):
	"""
	1) Split 32-bit number into 8 4-bit numbers
	2) Replace them by S table
	3) Attach again to 32bit number
	4) Rotate 11 bits left

	"""
	splitted_s = []
	swapped_num = ''
	swapped_32_bits = ''
	bits_arr = [int(bit) for bit in bin(number)[2:]]
	while len(bits_arr) < 32:
		bits_arr.insert(0, 0)

	for i in range(0, len(bits_arr), 4):
		num_4_bits = "".join([str(bit) for bit in bits_arr[i:i+4]])
		splitted_s.append(int(num_4_bits, 2))
	for i in range(8):
		swapped_num += bin(S[i][splitted_s[i]])[2:]

	if len(swapped_num) < 32:
		for _ in range(32 - len(swapped_num)):
			swapped_32_bits += "0"

	#11 bit cycle shift	
	swapped_32_bits += swapped_num
	swapped_32_bits = swapped_32_bits[11:32] + swapped_32_bits[0:11]
	return(swapped_32_bits)


def split_text(text):
	""" Split text into 8 byte parts """

	splitted_text = []
	for i in range(0, len(text), 8):
		splitted_text.append(text[i:i+8])
	if len(splitted_text[-1]) != 8:
		splitted_text[-1] = splitted_text[-1].ljust(8, ' ')
	return splitted_text


def encrypt_gamma_mod(text, key):
	gamma = chars_to_bits(key[0:64])
	splitted_text = split_text(text)
	encrypted_text = ''
	for i in range(len(splitted_text)):
		result_part = []
		bits_arr = chars_to_bits(splitted_text[i])
		enc_gamma = encrypt_part(gamma)
		for j in range(64):
			result_part.append(int(bits_arr[j]) ^ int(enc_gamma[j]))
		gamma = enc_gamma
		encrypted_text += bits_to_chars(result_part)
	return encrypted_text


def encrypt_gamma_feedback(text, key):
	gamma = chars_to_bits(key[0:64])
	splitted_text = split_text(text)
	encrypted_text = ''
	for i in range(len(splitted_text)):
		result_part = []
		bits_arr = chars_to_bits(splitted_text[i])
		enc_gamma = encrypt_part(gamma)
		for j in range(64):
			result_part.append(int(bits_arr[j]) ^ int(enc_gamma[j]))
		gamma = enc_gamma
		encrypted_text += bits_to_chars(result_part)
	return encrypted_text



def encrypt_part(bits):
	right = bits[32:64]
	left  = bits[0:32]
	for i in range(32):
		result_right = ''
		temp_right = (int(right, 2) + ALL_KEYS[K[i]]) % MOD
		temp_right = split_s(temp_right)  
		for j in range(32):
			result_right += str(int(left[j]) ^ int(temp_right[j]))
		left = right
		right = result_right
		#print("L : ", int(left, 2), " R: ", int(right, 2))
	return left + right


def decrypt_part(bits):
	right = bits[32:64]
	left  = bits[0:32]
	for i in range(31,-1,-1):
		result_left = ''
		temp_right = (int(left, 2) + ALL_KEYS[K[i]]) % MOD
		temp_right = split_s(temp_right)
		for j in range(32):
			result_left += str(int(right[j]) ^ int(temp_right[j]))
		right = left
		left = result_left
		#print("L : ", int(left, 2), " R: ", int(right, 2))
	return left + right


def decrypt(text, key):
	decrypt_text = ''
	splitted_text = split_text(text)
	for i in range(len(splitted_text)):
		bits_arr = chars_to_bits(splitted_text[i])
		bits_str = decrypt_part(bits_arr)
		decrypt_text += bits_to_chars(bits_str)
	return decrypt_text


def encrypt(text, key):
	encrypted_text = ''
	make_all_keys(key)
	splitted_text = split_text(text)
	for i in range(0, len(splitted_text)):
		bits_arr  = chars_to_bits(splitted_text[i])
		bits_str  = encrypt_part(bits_arr)
		encrypted_text += bits_to_chars(bits_str)
	return encrypted_text


def main():
	text = "aweWEWertuqwewqeqwweqwevqw12131313!@##$%^&"
	key = 'xab11122aabz1x22a2bb11333aib1124'
	enc_text = encrypt(text, key)
	dec_text = decrypt(enc_text, key)
	print("text : ", text)
	print("encrypted text", enc_text)
	print("decrypted text", dec_text)
	enc_gamma_text = encrypt_gamma_mod(text, key)
	dec_gamma_text = encrypt_gamma_mod(enc_gamma_text, key)
	print("enc gamma mod : ", enc_gamma_text)
	print("dec gamma mod : ", dec_gamma_text)
	enc_gamma_feedback_text = encrypt_gamma_feedback(text, key)
	dec_gamma_feedback_text = encrypt_gamma_feedback(enc_gamma_feedback_text, key)
	print("enc gamma mod with feedback: ", enc_gamma_feedback_text)
	print("dec gamma mod with feedback: ", dec_gamma_feedback_text)


if __name__ == '__main__':
	main()