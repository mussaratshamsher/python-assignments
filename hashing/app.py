import sys
import hashlib

# name = "Ali"
# print(hash(name))
# hash_1 = 617505771395200076
# hash_2 = 7382224314218100466
# hash_3 = -6677598580662364802
# print(hash_1 == hash_2)

# def hashfile(file):
#     BUF_SIZE = 65556
#     sha256 = hashlib.sha256()
#     with open("test.txt", 'rb') as f:
#         while True:
#             data = f.read(BUF_SIZE)
#             if not data:
#                 break
#             sha256.update(data)
#         return sha256.hexdigest()
# file_hash = hashfile(sys.argv[1])
# print(f"Hash:{file_hash}")        
    
import hashlib

string = b"My name is apple and I am a vegetable?"

sha256 = hashlib.sha256()
sha256.update(string)
string_hash = sha256.hexdigest()
print(f"Hash:{string_hash}")


