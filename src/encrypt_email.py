from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os
import sys
from src.utils import compute_email_size, read_text_file, write_text_file, read_binary_file, b64_encode

def encrypt(input="data/email_plain.txt",output="data/email_encrypted.txt",key="keys/aes_key.key", max_email_mb=25):
    if not os.path.exists(key):
        print(f"Key file not found: {key}")
        return
    key_bytes = read_binary_file(key)
        
    estimated_email_size = compute_email_size(input, block_size=AES.block_size, iv_size=16)
    if estimated_email_size > max_email_mb * 1024 * 1024:
        print(f"The size of email is {estimated_email_size / (1024 * 1024):.2f} MB, which is exceed {max_email_mb} MB limit.")
        return
    
    file_data = read_binary_file(input)
    cipher = AES.new(key_bytes, AES.MODE_CBC)
    cipher_text = cipher.encrypt(pad(file_data, AES.block_size))
    iv_and_cipher = cipher.iv + cipher_text
    encoded_cipher = b64_encode(iv_and_cipher)
    write_text_file(output, encoded_cipher)
    
    print(f"Email encrypted successfully!")
    
def main():
    # If no arguments provided, use defaults
    if len(sys.argv) == 1:
        encrypt()
    else:
        input_file = sys.argv[1] if len(sys.argv) > 1 else "data/email_plain.txt"
        output_file = sys.argv[2] if len(sys.argv) > 2 else "data/email_encrypted.txt"
        key_file = sys.argv[3] if len(sys.argv) > 3 else "keys/aes_key.key"
        max_email_mb = int(sys.argv[4]) if len(sys.argv) > 4 else 25

        encrypt(input_file, output_file, key_file, max_email_mb)

if __name__ == "__main__":
    main()