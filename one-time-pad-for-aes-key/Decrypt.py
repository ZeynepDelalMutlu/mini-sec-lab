import os

def read_key(filename, required_length=None):
    with open(filename, 'rb') as f:
        key = f.read()
    if required_length is not None:
        if len(key) < required_length:
            raise ValueError(f"OTP key should be at least {required_length} bytes, but there are only {len(key)} bytes!")
        # If the key length in the file is too big, read only the first 'required_length' from the file.
        return key[:required_length]
    return key

def otp_decrypt(ciphertext, otp_key):
    if len(ciphertext) != len(otp_key):
        raise ValueError("The length of AES key and OTP key must be the same!")
    return bytes(c ^ k for c, k in zip(ciphertext, otp_key))

def main():
    otp_key_filename = "otp_key.bin"                    # OTP key file path.
    encrypted_aes_filename = "encrypted_aes_key.bin"    # Encrypted AES key file path.
    aes_key_length = 32                                 # 256-bit = 32-byte

    # 1. Get OTP key from the file.
    otp_key = read_key(otp_key_filename, aes_key_length)
    
    # 2. Get encrypted AES key from the file.
    with open(encrypted_aes_filename, 'rb') as f:
        encrypted_aes_key = f.read()
    
    # 3. Decncrypt AES key by using OTP key.
    decrypted_aes_key = otp_decrypt(encrypted_aes_key, otp_key)
    print("Deşifrelenmiş AES anahtarı (hex):", decrypted_aes_key.hex())

if __name__ == "__main__":
    main()
