import os
import math
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

# This script derives a 256-bit AES key from a pre-shared secret using HKDF.
# Converts the integer shared secret to a bytes object.
def int_to_bytes(n: int) -> bytes:
    if n == 0:
        return b'\x00'
    byte_length = math.ceil(n.bit_length() / 8)
    return n.to_bytes(byte_length, byteorder='big')

# Uses HKDF with SHA-256 to derive a 32-byte (256-bit) AES key from the shared secret.
def derive_aes_key(shared_secret: int) -> bytes:
    secret_bytes = int_to_bytes(shared_secret)

    hkdf = HKDF(
        algorithm=hashes.SHA256(),      # Hash function
        length=32,                      # 256-bit key
        salt=None,                      # No salt for simplicity; in practice, use a random salt
        info=b'DH-derived AES key',     # Contextual information (can be empty)
        backend=default_backend()       # Cryptographic backend based on OpenSSL or others
    )
    return hkdf.derive(secret_bytes)

if __name__ == "__main__":
    # Read the shared secret (K1) from a file named "K1_PreSecretKey.txt"
    try:
        directory = os.path.dirname(__file__)  # Get the directory of the current file
        filepathPreSecretKey = os.path.join(directory, "K1_PreSecretKey.txt")
        with open(filepathPreSecretKey, "r") as f:
            k1_str = f.read().strip()
        k1 = int(k1_str)
    except Exception as e:
        print("Error reading the pre-secret key from file:", e)
        exit(1)
    
    aes_key = derive_aes_key(k1)

    # Save the derived AES key to a file
    filepathKey = os.path.join(directory, "aes_key.txt")
    with open(filepathKey, "wb") as f:
        f.write(aes_key)
        
    print("Derived AES 256-bit key (hex):", aes_key.hex())