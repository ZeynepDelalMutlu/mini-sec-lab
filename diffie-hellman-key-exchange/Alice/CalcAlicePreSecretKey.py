import os

def calculate_secret_key():
    
    n = 43  # Public parameter
    
    # Read Alice's private key (x)
    directory = os.path.dirname(__file__)  # Get the directory of the current file
    filepathPrivate = os.path.join(directory, "alice_private.txt")
    with open(filepathPrivate, "r") as f:
        x = int(f.read().strip())
    
    # Read Bob's public key (B)
    filepathPrivate = os.path.join(directory, "bob_public.txt")
    with open(filepathPrivate, "r") as f:
        B = int(f.read().strip())
    
    # Pre-Secret Key K1 = B^x mod n
    K1 = pow(B, x, n)

    # Save the Pre-Secret Key K1
    # under Alice's folder.
    filepathPrivate = os.path.join(directory, "K1_PreSecretKey.txt")
    with open(filepathPrivate, "w") as f:
        f.write(str(K1))
    print(f"Alice's pre-secret key (K1): {K1}")

if __name__ == "__main__":
    calculate_secret_key()
