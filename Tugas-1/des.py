# Implementasi sederhana algoritma DES dengan Python

# Tabel Permutasi Utama (Initial Permutation - IP)
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

# Tabel Permutasi Akhir (Final Permutation - FP)
FP = [40, 8, 48, 16, 56, 24, 64, 32,
      39, 7, 47, 15, 55, 23, 63, 31,
      38, 6, 46, 14, 54, 22, 62, 30,
      37, 5, 45, 13, 53, 21, 61, 29,
      36, 4, 44, 12, 52, 20, 60, 28,
      35, 3, 43, 11, 51, 19, 59, 27,
      34, 2, 42, 10, 50, 18, 58, 26,
      33, 1, 41, 9, 49, 17, 57, 25]

# Fungsi Permutasi (permute)
def permute(block, table):
    return ''.join([block[i - 1] for i in table])

# Fungsi untuk menghasilkan kunci (Key Generator)
def generate_keys(initial_key):
    # Asumsi kunci 64-bit, lalu diubah menjadi 16 sub-kunci 48-bit untuk setiap round
    sub_keys = []
    # Implementasi pengolahan kunci untuk setiap round
    for round in range(16):
        sub_key = initial_key[round % len(initial_key):] + initial_key[:round % len(initial_key)]
        sub_keys.append(sub_key[:48])
    return sub_keys

# Fungsi Fiestel untuk setiap round dalam DES
def feistel(right, sub_key):
    # Asumsi operasi sederhana, misalnya XOR
    return ''.join(['1' if right[i] != sub_key[i] else '0' for i in range(len(right))])

# Fungsi Enkripsi DES
def encrypt(plain_text, key):
    # Permutasi Awal
    permuted_text = permute(plain_text, IP)
    left, right = permuted_text[:32], permuted_text[32:]
    
    # Generate sub-kunci
    sub_keys = generate_keys(key)

    # 16 Round Fiestel
    for sub_key in sub_keys:
        new_right = feistel(right, sub_key)
        new_right, left = left, new_right  # Swap Left and Right
    
    # Penggabungan hasil setelah 16 round
    final_block = permute(left + right, FP)
    return final_block

# Fungsi Dekripsi DES
def decrypt(cipher_text, key):
    # Permutasi Awal
    permuted_text = permute(cipher_text, IP)
    left, right = permuted_text[:32], permuted_text[32:]
    
    # Generate sub-kunci
    sub_keys = generate_keys(key)

    # 16 Round Fiestel (dalam urutan terbalik untuk dekripsi)
    for sub_key in reversed(sub_keys):
        new_left = feistel(left, sub_key)
        new_left, right = right, new_left  # Swap Left and Right

    # Penggabungan hasil setelah 16 round
    final_block = permute(left + right, FP)
    return final_block

# Contoh Penggunaan
key = '1010101010111011000010010001100000100111001101101100110011011101'
plain_text = '0123456789ABCDEF'  # Harus dalam format bit (diubah dulu)

cipher_text = encrypt(plain_text, key)
print("Cipher Text:", cipher_text)

decrypted_text = decrypt(cipher_text, key)
print("Decrypted Text:", decrypted_text)
