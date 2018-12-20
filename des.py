IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

InvP = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]

P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]

PC_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]

PC_2 = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]


E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

SBOX = [
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
    ],
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
    ],
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
    ],
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
    ],
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
    ],
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
    ],

    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
     ],
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
    ]
]

SHIFT = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

ALLL_KEYS = []

def str_to_bitarray(s):
    bit_arr = list()
    for byte in s:
        bits = bin(byte)[2:] if isinstance(byte, int) else bin(ord(byte))[2:]
        while len(bits) < 8:
            bits = "0" + bits
        for bit in bits:
            bit_arr.append(int(bit))
    return bit_arr


def bitarray_to_str(bit_arr):
    result = ''
    for i in range(0, len(bit_arr), 8):
        byte = bit_arr[i:i + 8]
        s = ''.join([str(b) for b in byte])
        result = result + chr(int(s, 2))
    return result


def pc2(m_array):
    keyarray_48bit = []
    for i in range(0, len(PC_2)):
        keyarray_48bit.append(m_array[PC_2[i] - 1])
    return keyarray_48bit


def left_shift(m_array, round_num):
    num_shift = SHIFT[round_num]
    return m_array[num_shift:] + m_array[:num_shift]


def create_keys(key_text):
    key_bitarray = str_to_bitarray(key_text)
    perm_key_bitarray = []
    for i in range(0, len(PC_1)):  # из 64 в 56 бит
        perm_key_bitarray.append(key_bitarray[PC_1[i]])

    key_left = perm_key_bitarray[:28]
    key_right = perm_key_bitarray[28:]

    for i in range(0, 16):  # цикл. сдвиги влево
        key_left = left_shift(key_left, i)
        key_right = left_shift(key_right, i)
        ALLL_KEYS.append(pc2(key_left + key_right))  # вновь перемешиваем


def XOR(array_one, array_two):
    return [i ^ j for i, j in zip(array_one, array_two)]


def split_text(text, step):
    return [text[i:i + step] for i in range(0, len(text), step)]


def sbox_substition(m_array):
    sixbitarrays = split_text(m_array, 6)

    result = []
    s = ""

    for j in range(0, len(sixbitarrays)):
        row = int(str(sixbitarrays[j][0]) + str(sixbitarrays[j][5]), 2)
        col = int(str(sixbitarrays[j][1]) + str(sixbitarrays[j][2]) + str(sixbitarrays[j][3]) + str(sixbitarrays[j][4]), 2)
        sboxintvalue = SBOX[j][row][col]
        s = s + format(sboxintvalue, '04b')  # преобразуем в 4 бит
    for c in s:
        result.append(int(c))
    return result


def permute(m_array):
    permuted_array = []
    for i in range(0, len(P)):
        permuted_array.append(m_array[P[i] - 1])
    return permuted_array


def performRound(right_part, round_num):
    expanded_array = []
    for i in range(0, len(E)):  # расширяем до 48бит
        expanded_array.append(right_part[E[i] - 1])
    temp_array = XOR(expanded_array, ALLL_KEYS[round_num])  # xor с 48бит ключом
    sboxresult = sbox_substition(temp_array)  # из 48 бит в 32
    return permute(sboxresult)


def performRounds(m_array, is_encrypt):
    try:
        left_part = m_array[:32]
        right_part = m_array[32:]
        if is_encrypt:
            for i in range(0, 16):
                temp_array = right_part
                right_part = XOR(left_part, performRound(right_part, i))
                left_part = temp_array
            return right_part + left_part
        else:
            for i in range(16, 0, -1):
                temp_array = right_part
                right_part = XOR(left_part, performRound(right_part, i - 1))
                left_part = temp_array
        return right_part + left_part
    except:
        print("try again")


def ip_text(text, is_encrypt):
    try:
        perm_arr = IP if is_encrypt is False else InvP
        arr = []
        for i in range(0, len(perm_arr)):
            arr.append(text[perm_arr[i] - 1])
        return arr
    except:
        print("try again")


def encrypt(key_text, plain_text):
    create_keys(key_text)
    s = ""
    text_array = split_text(plain_text, 8)
    if len(plain_text) % 8 != 0:
        text_array[len(text_array) - 1] = str(text_array[len(text_array) - 1]).ljust(8, " ")
    for i in range(0, len(text_array)):
        s = s + encrypt_part(text_array[i])
    return s


def encrypt_part(text):
    str_bitarray = str_to_bitarray(text)
    temp_array = ip_text(str_bitarray, False)  #нач. перестановка
    round_performed_array = performRounds(temp_array, True)
    inv_perm_array = ip_text(round_performed_array, True)
    return bitarray_to_str(inv_perm_array)


def decrypt(encrypted_text, key_text):
    create_keys(key_text)
    s = ""
    dtext_array = split_text(encrypted_text, 8)
    for i in range(0, len(dtext_array)):
        s = s + decrypt_part(dtext_array[i])
    return s.rstrip()


def decrypt_part(enc_text):
    bit_array = str_to_bitarray(enc_text)
    inversed_array = ip_text(bit_array, False)
    temp_array = performRounds(inversed_array, False)
    straight_array = ip_text(temp_array, True)
    return bitarray_to_str(straight_array)


def main():
    text = "abcdabcd1"
    key = "12312333"
    encrypt(key, text)
    tt = encrypt(key, text)
    print("result ", tt)
    gg = decrypt(tt, key)
    print("decrypt ", gg)


if __name__ == "__main__":
    main()
