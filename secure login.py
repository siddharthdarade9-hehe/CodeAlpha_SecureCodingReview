import hashlib

user = "admin"
stored_password = hashlib.sha256("admin123".encode()).hexdigest()

username = input("Username: ")
password = hashlib.sha256(input("Password: ").encode()).hexdigest()

if username == user and password == stored_password:
    print("Login Successful")
else:
    print("Login Failed")