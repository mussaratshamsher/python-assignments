

#Hashing

def hash(password):
    sha256(password.encode()).hexdigest()

pass1 = "1"
pass2 = "2"
pass3 = "3"

print(hash(pass1))
print(hash(pass2))
print(hash(pass3))  

# credentials = {
#     "pass1":
# }

user_input = str(input("enter your password: "))

if user_input == credentials["pass1"]:
    print("password is correct")
else:
    print("access denied")
