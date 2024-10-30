import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Fungsi untuk dekripsi pesan
def decrypt_message(encrypted_message, key):
    iv = encrypted_message[:AES.block_size]  # Ekstrak iv
    ciphertext = encrypted_message[AES.block_size:]  # Ekstrak ciphertext
    cipher = AES.new(key, AES.MODE_CBC, iv)  # Buat objek cipher
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)  # Dekripsi dan unpad
    return decrypted_message.decode()

# Inisialisasi server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("Menunggu koneksi dari client...")

# Terima koneksi dari client
conn, addr = server_socket.accept()
print(f"Koneksi diterima dari {addr}")

# Terima kunci dan pesan terenkripsi dari client
key = conn.recv(16)
encrypted_message = conn.recv(1024)  # Ubah sesuai ukuran pesan

# Dekripsi pesan
decrypted_message = decrypt_message(encrypted_message, key)
print("Pesan terdekripsi dari client:", decrypted_message)

# Tutup koneksi
conn.close()
server_socket.close()
