import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

# Fungsi untuk enkripsi pesan
def encrypt_message(message, key):
    cipher = AES.new(key, AES.MODE_CBC)  # Mode CBC
    iv = cipher.iv  # Inisialisasi vektor
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))  # Pad dan enkripsi
    return iv + ciphertext  # Gabungkan iv dan ciphertext untuk dikirim

# Kunci AES harus 16, 24, atau 32 byte
key = get_random_bytes(16)
message = "Ini adalah pesan terenkripsi dari client!"

# Enkripsi pesan
encrypted_message = encrypt_message(message, key)

# Koneksi ke server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

# Kirim kunci dan pesan terenkripsi
client_socket.sendall(key)
client_socket.sendall(encrypted_message)

# Tutup koneksi
client_socket.close()
print("Pesan terenkripsi telah dikirim ke server.")
