from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import math

def email_size(data_size, block_size=16, base64_overhead=1.33):
    padding = block_size - (data_size % block_size) if data_size % block_size != 0 else 0
    encrypted_size = data_size + padding
    return math.ceil(encrypted_size * base64_overhead)

def encrypt(input="data/email_plain.txt",output="data/email_encrypted.txt",key="keys/aes_key.key"):
    with open(key,"rb") as k:
        key=k.read()
        
    with open(input,"r",encoding="utf-8") as i:
        plain_text = i.read()
        
    cipher = AES.new(key, AES.MODE_CBC)
    ini_vector = cipher.iv
    
    # padding data
    plain_text_padded = pad(plain_text.encode("utf-8"), AES.block_size)
    
    #compute email size
    estimated_email_size = email_size(len(plain_text_padded))
    if estimated_email_size > 25 * 1024 * 1024: # = 25MB
        print(f"The size of email is too large!!!")
        return 
    
    # encrypt data
    cipher_text = cipher.encrypt(plain_text_padded)
    result = base64.b64encode(ini_vector + cipher_text).decode("utf-8")
    
    # store result
    with open(output, "w", encoding="utf-8") as o:
        o.write(result)
    
    print(f"Email encrypted successfully!")
    
encrypt() 