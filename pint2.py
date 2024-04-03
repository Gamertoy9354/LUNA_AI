from cryptography.fernet import Fernet
# Generate a key
key = b'2AbgwdSql-1lzi0u6RN56G8PH7ALq4db84SnfpnGMeA='
cipher_suite = Fernet(key)

with open('/home/shis/Desktop/LunaAI/test/password_file.txt', 'r') as file:
    # Read the password from the file
    password = file.readline().strip()

password_bytes = password.encode()

decrypted_text = cipher_suite.decrypt(password_bytes)

decpass = decrypted_text.decode()



upass = str(input("Please enter the password to continue: "))
