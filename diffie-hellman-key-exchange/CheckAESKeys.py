import os

def read_aes_key(filepath: str) -> str:
    with open(filepath, "rb") as f:
        key = f.read().strip()
    return key

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # AES-key paths
    alice_key_path = os.path.join(base_dir, "Alice", "aes_key.txt")
    bob_key_path   = os.path.join(base_dir, "Bob", "aes_key.txt")

    try:
        alice_key = read_aes_key(alice_key_path)
    except Exception as e:
        print(f"Alice's key could not be read ({alice_key_path}): {e}")
        return

    try:
        bob_key = read_aes_key(bob_key_path)
    except Exception as e:
        print(f"Bob's key could not be read ({bob_key_path}): {e}")
        return

    # Anahtarları ekrana yazdır ve karşılaştır
    print("Alice's AES key:", alice_key)
    print("Bob's AES key:  ", bob_key)

    if alice_key == bob_key:
        print("Success! AES keys are matched!")
    else:
        print("Error! AES keys are NOT matched!")

if __name__ == "__main__":
    main()
