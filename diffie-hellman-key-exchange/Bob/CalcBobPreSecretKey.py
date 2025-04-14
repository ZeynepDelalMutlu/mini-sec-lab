import os

def calculate_secret_key():
    
    n = 43  # Public parameter
    
    # Read Bob's private key (y)
    directory = os.path.dirname(__file__)  # Get the directory of the current file
    filepathPrivate = os.path.join(directory, "bob_private.txt")
    with open(filepathPrivate, "r") as f:
        y = int(f.read().strip())
    
    # Read Alice's public key (A)
    filepathPrivate = os.path.join(directory, "alice_public.txt")
    with open(filepathPrivate, "r") as f:
        A = int(f.read().strip())
    
    # Pre-Secret Key K2 = A^y mod n
    K2 = pow(A, y, n)

    # Save the Pre-Secret Key K2
    # under Bob's folder.
    filepathPrivate = os.path.join(directory, "K2_PreSecretKey.txt")
    with open(filepathPrivate, "w") as f:
        f.write(str(K2))
    print(f"Bob's pre-secret key (K2): {K2}")

if __name__ == "__main__":
    calculate_secret_key()
