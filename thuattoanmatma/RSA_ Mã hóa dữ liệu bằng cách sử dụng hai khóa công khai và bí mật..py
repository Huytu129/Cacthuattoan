import rsa

def rsa_encrypt_decrypt():
    # Generate RSA keys
    public_key, private_key = rsa.newkeys(512)

    # Original message
    message = "This is a secret message".encode()

    # Encrypt the message
    encrypted_message = rsa.encrypt(message, public_key)

    # Decrypt the message
    decrypted_message = rsa.decrypt(encrypted_message, private_key).decode()

    return message, encrypted_message, decrypted_message

# Example usage:
original_message, encrypted_message, decrypted_message = rsa_encrypt_decrypt()

print(f"Original message: {original_message}")
print(f"Encrypted message (hex): {encrypted_message.hex()}")
print(f"Decrypted message: {decrypted_message}")
