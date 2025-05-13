from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

# Step 1: Generate RSA keys
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Step 2: Encrypt a message using the public key
def encrypt_message(message, public_key):
    cipher = PKCS1_OAEP.new(public_key)
    encrypted = cipher.encrypt(message.encode())
    return base64.b64encode(encrypted).decode()

# Step 3: Decrypt the message using the private key
def decrypt_message(encrypted_message, private_key):
    cipher = PKCS1_OAEP.new(private_key)
    decoded = base64.b64decode(encrypted_message)
    decrypted = cipher.decrypt(decoded)
    return decrypted.decode()

# Example usage
message = "RSA is a public key algorithm."
print("Original Message:", message)

encrypted_msg = encrypt_message(message, public_key)
print("Encrypted Message:", encrypted_msg)

decrypted_msg = decrypt_message(encrypted_msg, private_key)
print("Decrypted Message:", decrypted_msg)
