

#✍🎨Task: print the message "Kharak Singh k kharakny se kharakti hain khirkiyan." 5 times

#  1. Using a for loop:
print("using for loop:")
for _ in range(5):
  print("Kharak Singh k kharakny se kharakti hain khirkiyan")

#  2. Using while loop:
print("\n using while loop:")
count = 0
while count < 5:
  print("Kharak Singh k kharakny se kharakti hain khirkiyan")
  count +=1

# 3.  Using list comprehension with join
print("\n using list comprehension with join")
print("\n".join(["Kharak Singh k kharakny se kharakti hain khirkiyan."]*5))

# 4.Using * operator for repetition:
print(" \n using * operator for repetition:")
print(("Kharak Singh k kharakny se kharakti hain khirkiyan.\n"*5).strip())

