import secrets
import shutil
import os

# Public parameters. In real applications, these should be agreed upon by both parties.
# mod (prime number), generator (primitive root) values are usually large primes.
n = 43  # Common mod (prime number)
g = 7   # Generator (primitive root)

# Generate private key for Bob 'x': 2 <= x <= n-1
y = secrets.randbelow(n - 2) + 2
# Public key for Bob: A = g^x mod n
B = pow(g, y, n)

# Save Bob private key under her own folder.
directory = os.path.dirname(__file__)  # Get the directory of the current file
filepathPrivate = os.path.join(directory, "bob_private.txt")
with open(filepathPrivate, "w") as f:
    f.write(str(y))

# Save Bob public key (B) under her own folder.
filepathPublic = os.path.join(directory, "bob_public.txt")
with open(filepathPublic, "w") as f:
    f.write(str(B))

print(f"Bob's private key (y): {y}")
print(f"Bob's public key (B): {B}")

# Copy the public key of (B) Bob under the Alice's folder.
# In real scenario public key B is sent to Alice.
try:
    alice_directory = os.path.join(directory, "..", "Alice/bob_public.txt")
    shutil.copy(filepathPublic, alice_directory)
    print("Bob's public key successfully copied to Alice's folder.")
except Exception as e:
    print("Error copying Bob's public key to Alice's folder:", e)