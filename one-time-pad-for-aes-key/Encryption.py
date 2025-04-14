import os

def read_otp_key(filename, required_length):
    with open(filename, 'rb') as f:
        key = f.read()
    if len(key) < required_length:
        raise ValueError(f"OTP key should be at least {required_length} bytes, but there are only {len(key)} bytes!")
    # If the key length in the file is too big, read only the first 'required_length' from the file.
    return key[:required_length]

def otp_encrypt(aes_key, otp_key):
    if len(aes_key) != len(otp_key):
        raise ValueError("The length of AES key and OTP key must be the same!")
    # XOR: for each byte.
    return bytes(a ^ b for a, b in zip(aes_key, otp_key))

def main():
    # Settings:
    otp_key_filename = "otp_key.bin"                    # OTP key file path.
    encrypted_aes_filename = "encrypted_aes_key.bin"    # Encrypted AES key file path.
    aes_key_length = 32                                 # 256-bit = 32-byte

    # 1. Get OTP key.
    try:
        otp_key = read_otp_key(otp_key_filename, aes_key_length)
    except Exception as e:
        print("OTP key could not be read:", e)
        return

    # 2. Determine the AES key.
    # In the real life scenario, AES key is generated in different way.
    # Here, a random 256-bit is generated to represent AES-256 key.
    # aes_key = os.urandom(aes_key_length)
    # Or it is possible to generate a constant AES key :
    aes_key = b'\x01\x23\x45\x67' *8

    print("AES key (hex):", aes_key.hex())
    print("OTP key (hex):", otp_key.hex())

    # 3. Encrypt AES key by using OTP key.
    encrypted_aes_key = otp_encrypt(aes_key, otp_key)
    print("Encrypted AES key (hex):", encrypted_aes_key.hex())

    # 4. Save the encrypted AES key in a file.
    with open(encrypted_aes_filename, "wb") as f:
        f.write(encrypted_aes_key)
    print(f"Encrypted AES key saved in the file '{encrypted_aes_filename}'.")

if __name__ == "__main__":
    main()