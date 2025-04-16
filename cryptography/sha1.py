from hashlib import sha1

message = input("Enter message: ")
hash_object = sha1(message.encode())
print("SHA-1 Digest:", hash_object.hexdigest()) 