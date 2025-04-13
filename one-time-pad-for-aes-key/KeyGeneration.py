import os
import binascii

class OTPKeyGenerator:
    def __init__(self, length):
        self.length = length

    ###
    # KEY GENERATOR is:
    ###
    def generate_key(self):
        return os.urandom(self.length)

    def save_key(self, filename, key):
        with open(filename, 'wb') as f:
            f.write(key)
        return key

if __name__ == "__main__":
    key_length = 32  # 32-byte = 256-bit
    key_gen = OTPKeyGenerator(key_length)
    
    # Print key
    key = key_gen.generate_key()
    print("Key (binary):", key)

    hex_key = binascii.b2a_hex(key).decode('utf-8')
    print("Key (hex):", hex_key)
    
    # Save the key in a file
    key_gen.save_key("otp_key.bin", key)
    print("The key is saved.")