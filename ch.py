password = input("Enter your password: ")
count = 0
for ch in password:
       if ch.islower():
        count += 1

print("Number of lowercase characters in the password:", count)