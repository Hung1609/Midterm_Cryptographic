from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64
import os

def decrypt(input="data/email_encrypted.txt", output="data/email_decrypted.txt", key="keys/aes_key.key"):
    with open(key, "rb") as k:
        key = k.read()
        
    with open(input, "r", encoding="utf-8") as i:
        encoded_data = i.read()
    
    data = base64.b64decode(encoded_data)
    init_vector = data[:16]
    cipher_text = data[16:]
    
    cipher = AES.new(key, AES.MODE_CBC, iv=init_vector)
    
    plain_data_padded = cipher.decrypt(cipher_text)
    try:
        plain_data = unpad(plain_data_padded, AES.block_size).decode("utf-8")
        with open(output, "w", encoding="utf-8") as o:
            o.write(plain_data)
        print(f"File decrypted successfully as text! Output saved to {output}")
    except UnicodeDecodeError:
        plain_data = unpad(plain_data_padded, AES.block_size)
        with open(output, "wb") as o:
            o.write(plain_data)
        print(f"File decrypted successfully as binary! Output saved to {output}")

decrypt()
