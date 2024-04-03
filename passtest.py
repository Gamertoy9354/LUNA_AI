from cryptography.fernet import Fernet

# Generate a key
key = b'2AbgwdSql-1lzi0u6RN56G8PH7ALq4db84SnfpnGMeA='
cipher_suite = Fernet(key)
print(key)



# Text to encrypt
text = "shismehta/@9354"

# Encrypt the text
encrypted_text = cipher_suite.encrypt(text.encode())

# Print or save the encrypted text
print("Encrypted text:", encrypted_text.decode())

decrypted_text = cipher_suite.decrypt(encrypted_text)

print("PASSWORD: ",decrypted_text)
