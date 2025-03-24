# Problem Statement
# You want to be safe online and use different passwords for different websites. However, you are forgetful at times 
# and want to make a program that can match which password belongs to which website without storing the actual password!

# This can be done via something called hashing. Hashing is when we take something and convert it into a different,
# unique identifier.This is done using a hash function. Luckily, there are several resources that can help us with this.

# solution
from hashlib import sha256

def login(email, stored_logins, password_to_check):
    if stored_logins[email] == hash_password(password_to_check):
        return True
    return False

def hash_password(password):
    return sha256(password.encode()).hexdigest()

def main():
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8", # hash of correct_password_1
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc", # hash of correct_password_2
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb" # hash of correct_password_3
    }
    print(login("example@gmail.com", stored_logins, "correct_password_1"))
    print(login("code_in_placer@cip.org", stored_logins, "correct_password_2"))
    print(login("student@stanford.edu", stored_logins, "correct_password_3"))

main()
