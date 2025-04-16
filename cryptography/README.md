# Cryptography Programs

This repository contains implementations of various cryptographic algorithms in Python. Each program demonstrates a different encryption/decryption technique.

## Dependencies

To run these programs, you'll need to install the following packages:
```bash
pip install numpy pycryptodome
```

## Implemented Ciphers

### 1. Hill Cipher
The Hill Cipher is a polygraphic substitution cipher based on linear algebra. It works by:
- Converting the plaintext into numerical vectors
- Using matrix multiplication with a key matrix to encrypt the text
- The key must be a square matrix with a determinant that has an inverse modulo 26
- The text is divided into blocks matching the size of the key matrix
- Each block is multiplied by the key matrix modulo 26
- The resulting numbers are converted back to letters

Implementation:
- Uses NumPy for matrix operations
- Handles 2x2 key matrices
- Converts text to uppercase and removes spaces
- Pads with 'X' if text length is odd
- Uses modular arithmetic for encryption/decryption

[View Code](https://github.com/mccleod1290/PyPlayground/blob/main/cryptography/hill_cipher.py)

### 2. Vigenère Cipher
The Vigenère Cipher is a polyalphabetic substitution cipher that:
- Uses a keyword to determine the shift for each letter
- Repeats the keyword to match the length of the plaintext
- Shifts each letter by the corresponding letter in the keyword
- Provides better security than simple substitution ciphers
- Can be broken using frequency analysis if the keyword is short

Implementation:
- Uses ASCII values for character manipulation
- Handles both uppercase and lowercase letters
- Implements modular arithmetic for shifting
- Preserves non-alphabetic characters
- Supports variable-length keywords

[View Code](https://github.com/mccleod1290/PyPlayground/blob/main/cryptography/vigenere_cipher.py)

### 3. Rail Fence Cipher
The Rail Fence Cipher is a transposition cipher that:
- Writes the message in a zigzag pattern along a number of "rails"
- Reads the message row by row to create the ciphertext
- The number of rails is the key
- Provides security through rearrangement rather than substitution
- Can be broken by trying different numbers of rails

Implementation:
- Uses nested lists to represent the rail fence
- Implements zigzag pattern using direction changes
- Handles encryption and decryption using matrix operations
- Supports variable number of rails
- Preserves message length

[View Code](https://github.com/mccleod1290/PyPlayground/blob/main/cryptography/rail_fence.py)

### 4. DES (Data Encryption Standard)
DES is a symmetric-key block cipher that:
- Uses a 56-bit key to encrypt 64-bit blocks of data
- Applies 16 rounds of substitution and permutation
- Uses Feistel network structure
- Includes initial and final permutations
- Has been replaced by AES for modern applications

Implementation:
- Uses pycryptodome library for DES operations
- Implements ECB mode encryption
- Handles padding for messages not aligned to block size
- Supports 8-character keys
- Converts between hex and bytes for output

[View Code](https://github.com/mccleod1290/PyPlayground/blob/main/cryptography/des.py)

### 5. AES (Advanced Encryption Standard)
AES is a symmetric encryption algorithm that:
- Uses a block size of 128 bits
- Supports key sizes of 128, 192, or 256 bits
- Applies multiple rounds of substitution and permutation
- Uses a substitution-permutation network
- Is the current industry standard for symmetric encryption

Implementation:
- Uses pycryptodome for AES operations
- Implements CBC mode with random IV
- Generates random 16-byte keys
- Handles message padding
- Combines IV with ciphertext for storage

[View Code](https://github.com/mccleod1290/PyPlayground/blob/main/cryptography/aes.py)

### 6. RSA Algorithm
RSA is an asymmetric cryptographic algorithm that:
- Uses a public key for encryption and a private key for decryption
- Relies on the difficulty of factoring large numbers
- Generates keys using large prime numbers
- Provides secure key exchange and digital signatures
- Is widely used in secure communications

Implementation:
- Uses pycryptodome for RSA operations
- Generates 2048-bit keys
- Implements OAEP padding for encryption
- Handles key generation and management
- Supports message encryption and decryption

[View Code](https://github.com/mccleod1290/PyPlayground/blob/main/cryptography/rsa.py)

### 7. Diffie-Hellman Key Exchange
The Diffie-Hellman key exchange:
- Allows two parties to establish a shared secret key
- Uses modular exponentiation
- Relies on the difficulty of the discrete logarithm problem
- Enables secure key exchange over public channels
- Forms the basis for many secure communication protocols

Implementation:
- Uses fixed prime and generator values
- Implements modular exponentiation
- Calculates public and private keys
- Computes shared secret
- Demonstrates key agreement between two parties

[View Code](https://github.com/mccleod1290/PyPlayground/blob/main/cryptography/diffie_hellman.py)

### 8. SHA-1 Message Digest
SHA-1 is a cryptographic hash function that:
- Produces a 160-bit hash value
- Processes input in 512-bit blocks
- Uses a series of logical operations
- Creates a unique digital fingerprint
- Is used for data integrity verification

Implementation:
- Uses Python's hashlib library
- Handles string input
- Produces hexadecimal output
- Supports variable-length messages
- Demonstrates one-way hashing

[View Code](https://github.com/mccleod1290/PyPlayground/blob/main/cryptography/sha1.py)

### 9. Digital Signature Standard (DSS)
DSS is a standard for digital signatures that:
- Uses the Digital Signature Algorithm (DSA)
- Creates and verifies digital signatures
- Ensures message authenticity and integrity
- Uses modular exponentiation
- Provides non-repudiation

Implementation:
- Uses pycryptodome for DSA operations
- Generates 2048-bit keys
- Implements signature generation and verification
- Handles message hashing
- Demonstrates signature validation

[View Code](https://github.com/mccleod1290/PyPlayground/blob/main/cryptography/dss.py)

### 10. Caesar Cipher
The Caesar Cipher is a simple substitution cipher that:
- Shifts each letter by a fixed number down the alphabet
- Uses a single key for the entire message
- Is easily broken by frequency analysis
- Preserves letter frequency patterns
- Is useful for learning basic cryptography concepts

Implementation:
- Uses ASCII values for character shifting
- Preserves case sensitivity
- Handles non-alphabetic characters
- Supports both encryption and decryption
- Implements modular arithmetic for wrapping

[View Code](https://github.com/mccleod1290/PyPlayground/blob/main/cryptography/caesar.py)

### 11. Playfair Cipher
The Playfair Cipher is a digraph substitution cipher that:
- Encrypts pairs of letters instead of single letters
- Uses a 5x5 grid of letters (I and J share a cell)
- Has specific rules for handling repeated letters
- Provides better security than simple substitution
- Was used by the British in World War I

Implementation:
- Creates 5x5 key matrix from keyword
- Handles digraph encryption/decryption
- Implements special rules for same-letter pairs
- Uses matrix operations for cipher operations
- Preserves message structure

[View Code](https://github.com/mccleod1290/PyPlayground/blob/main/cryptography/playfair.py)

### 12. One-Time Pad
The One-Time Pad is a theoretically unbreakable cipher that:
- Uses a random key as long as the message
- Applies the key only once
- Requires perfect randomness in the key
- Provides perfect secrecy when used correctly
- Is impractical for most applications due to key distribution

Implementation:
- Generates random keys using Python's random module
- Uses modular arithmetic for encryption
- Handles variable-length messages
- Implements perfect secrecy
- Demonstrates key generation and usage

[View Code](https://github.com/mccleod1290/PyPlayground/blob/main/cryptography/one_time_pad.py)

## Usage

Each program can be run independently and will prompt for the necessary input. The programs demonstrate both encryption and decryption where applicable.

## Security Note

While these implementations demonstrate the concepts of various cryptographic algorithms, they should not be used for production systems without proper security review and hardening. 