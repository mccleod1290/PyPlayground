from Crypto.Protocol.KDF import HKDF
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes

def generate_shared_key(private_key, public_key, prime):
    return pow(public_key, private_key, prime)

prime = 23
base = 5

alice_private = int(input("Enter Alice's private key: "))
bob_private = int(input("Enter Bob's private key: "))

alice_public = pow(base, alice_private, prime)
bob_public = pow(base, bob_private, prime)

alice_shared = generate_shared_key(alice_private, bob_public, prime)
bob_shared = generate_shared_key(bob_private, alice_public, prime)

print("Alice's shared key:", alice_shared)
print("Bob's shared key:", bob_shared) 