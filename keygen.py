from cryptography.fernet import Fernet

# Generate a random encryption key
key = Fernet.generate_key()

# Print the generated key
print("Generated encryption key:", key)
