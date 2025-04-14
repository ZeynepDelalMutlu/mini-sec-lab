import secrets
import shutil
import os

# Public parameters. In real applications, these should be agreed upon by both parties.
# mod (prime number), generator (primitive root) values are usually large primes.
n = 43  # Common mod (prime number)
g = 7   # Generator (primitive root)

# Generate private key for Alice 'x': 2 <= x <= n-1
x = secrets.randbelow(n - 2) + 2
# Public key for Alice: A = g^x mod n
A = pow(g, x, n)

# Save Alice private key under her own folder.
directory = os.path.dirname(__file__)  # Get the directory of the current file
filepathPrivate = os.path.join(directory, "alice_private.txt")
with open(filepathPrivate, "w") as f:
    f.write(str(x))

# Save Alice public key (A) under her own folder.
filepathPublic = os.path.join(directory, "alice_public.txt")
with open(filepathPublic, "w") as f:
    f.write(str(A))

print(f"Alice's private key (x): {x}")
print(f"Alice's public key (A): {A}")

# Copy the public key of (A) Alice under the Bob's folder.
# In real scenario public key A is sent to Bob.
try:
    bob_directory = os.path.join(directory, "..", "Bob/alice_public.txt")
    shutil.copy(filepathPublic, bob_directory)
    print("Alice's public key successfully copied to Bob's folder.")
except Exception as e:
    print("Error copying Alice's public key to Bob's folder:", e)