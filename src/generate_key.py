from Crypto.Random import get_random_bytes

def generate_aes_key(file_path="keys/aes_key.key", key_size=32):
    key = get_random_bytes(key_size)
    with open(file_path,"wb") as key_file:
        key_file.write(key)
    print(f"AES key generated successfully and saved to {file_path}")
    
generate_aes_key()