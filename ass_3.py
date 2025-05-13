# pip install pycryptodome
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

# AES uses block size of 16 bytes
BLOCK_SIZE = 16

def encrypt_AES(plain_text, key):
    # Convert plain text to bytes
    data = plain_text.encode('utf-8')
    
    # Generate a random 16-byte IV
    iv = get_random_bytes(BLOCK_SIZE)
    
    # Create AES cipher in CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Pad and encrypt the data
    encrypted_bytes = cipher.encrypt(pad(data, BLOCK_SIZE))
    
    # Return IV + encrypted text, base64 encoded
    return base64.b64encode(iv + encrypted_bytes).decode('utf-8')

def decrypt_AES(enc_text, key):
    # Decode the base64 encoded string
    raw = base64.b64decode(enc_text)
    
    # Extract IV and encrypted data
    iv = raw[:BLOCK_SIZE]
    encrypted_bytes = raw[BLOCK_SIZE:]
    
    # Create AES cipher with same IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Decrypt and unpad
    decrypted = unpad(cipher.decrypt(encrypted_bytes), BLOCK_SIZE)
    
    return decrypted.decode('utf-8')


# Example usage
if __name__ == "__main__":
    # AES key must be either 16, 24, or 32 bytes long
    key = b'ThisIsA16ByteKey'  # Example 16-byte key
    
    message = "This is a secret message."
    print("Original Message:", message)

    encrypted = encrypt_AES(message, key)
    print("Encrypted:", encrypted)

    decrypted = decrypt_AES(encrypted, key)
    print("Decrypted:", decrypted)
