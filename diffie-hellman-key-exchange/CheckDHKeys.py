import os

def check_dh_keys():
    
    # Alice pre-secret key
    directory = os.path.dirname(__file__)  # Get the directory of the current file
    K1_file = os.path.join(directory, "Alice/K1_PreSecretKey.txt")
    with open(K1_file, "r") as f:
        K1 = int(f.read().strip())
    
    # Bob pre-secret key
    K2_file = os.path.join(directory, "Bob/K2_PreSecretKey.txt")
    with open(K2_file, "r") as f:
        K2 = int(f.read().strip())

    print(f"Alice's secret key (K1): {K1}")
    print(f"Bob's secret key (K2): {K2}")

    if K1 == K2:
        print("Success: Alice and Bob found the same pre-secret keys!")
    else:
        print("Error: Alice and Bob CANNOT find the same pre-secret keys!")

if __name__ == "__main__":
    check_dh_keys()