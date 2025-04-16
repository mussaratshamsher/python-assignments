
# Fernet module is imported from the cryptography package
from cryptography.fernet import Fernet 

# key is generated
key = Fernet.generate_key()
f = Fernet(key) # storing key in a variable

# plaintext into ciphertext
token = f.encrypt(b"Welcome to wonderland!")
print(token)
print(len(token))

# ciphertext into plaintext
d = f.decrypt(token)
print(d.decode())

