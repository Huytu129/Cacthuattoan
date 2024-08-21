from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import base64


def encrypt_message(message, key):
    # Tạo nonce cho chế độ GCM
    nonce = os.urandom(12)  # AES-GCM yêu cầu nonce dài 12 byte

    # Tạo cipher object với AES chế độ GCM
    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce), backend=default_backend())
    encryptor = cipher.encryptor()

    # Mã hóa dữ liệu
    ciphertext = encryptor.update(message) + encryptor.finalize()
    tag = encryptor.tag

    # Trả về dữ liệu đã mã hóa, nonce và tag dưới dạng base64
    return base64.b64encode(ciphertext).decode(), base64.b64encode(tag).decode(), base64.b64encode(nonce).decode()


def decrypt_message(ciphertext_b64, tag_b64, nonce_b64, key):
    ciphertext = base64.b64decode(ciphertext_b64)
    tag = base64.b64decode(tag_b64)
    nonce = base64.b64decode(nonce_b64)

    # Tạo cipher object với AES chế độ GCM
    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce, tag), backend=default_backend())
    decryptor = cipher.decryptor()

    # Giải mã dữ liệu
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()

    return decrypted_data.decode()


# Tạo khóa bí mật (16 bytes cho AES-128)
key = os.urandom(16)

# Dữ liệu để mã hóa
message = b"Secret data that needs encryption"

# Mã hóa dữ liệu
ciphertext_b64, tag_b64, nonce_b64 = encrypt_message(message, key)
print("Ciphertext:", ciphertext_b64)
print("Tag:", tag_b64)
print("Nonce:", nonce_b64)

# Giải mã dữ liệu
decrypted_message = decrypt_message(ciphertext_b64, tag_b64, nonce_b64, key)
print("Decrypted data:", decrypted_message)
