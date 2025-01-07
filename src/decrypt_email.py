from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64
import os
import sys
from src.utils import read_text_file, write_binary_file, write_text_file, read_binary_file, b64_decode

def decrypt(input="data/email_encrypted.txt", output="data/email_decrypted.txt", key="keys/aes_key.key"):
    if not os.path.exists(key):
        print(f"Key file not found: {key}")
        return
    key_bytes = read_binary_file(key)
    
    if not os.path.exists(input):
        print(f"Encrypted file not found: {input}")
        return
    try:
        encoded_data = read_text_file(input)
    except Exception as e:
        print(f"Error reading ciphertext: {str(e)}")
        return
    
    try:
        data = b64_decode(encoded_data)
    except Exception as e:
        print(f"Failed to Base64-decode the data: {str(e)}")
        return 
    
    init_vector = data[:16]
    cipher_text = data[16:]
        
    try:
        cipher = AES.new(key_bytes, AES.MODE_CBC, iv=init_vector)    
        plain_data_padded = cipher.decrypt(cipher_text)
    except Exception as e:
        print(f"Decryption failed: {str(e)}")
        return
    
    try:
        plain_data_bytes = unpad(plain_data_padded, AES.block_size)
    except Exception as e:
        print(f"Unpadding failed: {str(e)}")
        return
    
    try:
        plain_text = plain_data_bytes.decode("utf-8")
        write_text_file(output, plain_text)
        print(f"File decrypted successfully as text!")
    except UnicodeDecodeError:
        write_binary_file(output, plain_data_bytes)
        print(f"File decrypted successfully as binary!")
        
def main():
    # If no arguments provided, use defaults
    if len(sys.argv) == 1:
        decrypt()
    else:
        input_file = sys.argv[1] if len(sys.argv) > 1 else "data/email_encrypted.txt"
        output_file = sys.argv[2] if len(sys.argv) > 2 else "data/email_decrypted.txt"
        key_file = sys.argv[3] if len(sys.argv) > 3 else "keys/aes_key.key"

        decrypt(input_file, output_file, key_file)

if __name__ == "__main__":
    main()
