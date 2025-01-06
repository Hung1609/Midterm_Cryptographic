from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import os
import math

def email_size(file_path, block_size=AES.block_size, iv_size=16):
    file_size = os.path.getsize(file_path)
    padded_size = (file_size + block_size - 1) // block_size * block_size
    encrypted_size = iv_size + padded_size
    base64_size = (encrypted_size + 2) // 3*4
    return base64_size

def encrypt(input="data/email_pdf.pdf",output="data/email_encrypted.txt",key="keys/aes_key.key"):
    with open(key,"rb") as k:
        key=k.read()
        
    with open(input,"rb") as i:
        file_data = i.read()
        
    #compute email size
    estimated_email_size = email_size(input)
    if estimated_email_size > 25 * 1024 * 1024: # = 25MB
        print(f"The size of email is {estimated_email_size / (1024 * 1024):.2f} MB")
        return   
    
    cipher = AES.new(key, AES.MODE_CBC)
    ini_vector = cipher.iv
    
    # padding data
    file_data_padded = pad(file_data, AES.block_size)
    
    # encrypt data
    cipher_text = cipher.encrypt(file_data_padded)
    result = base64.b64encode(ini_vector + cipher_text).decode("utf-8")
    
    # store result
    with open(output, "w", encoding="utf-8") as o:
        o.write(result)
    
    print(f"Email encrypted successfully!")
    
encrypt() 