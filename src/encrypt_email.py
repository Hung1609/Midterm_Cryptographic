from Crypto.Cipher import AES
import base64

def encrypt(input="emails/email_plain.txt",output="emails/email_encrypted.txt",key="keys/aes_key.key"):
    with open(key,"rb") as k:
        key=k.read()
        
    with open(input,"r",encoding="utf-8") as i:
        plain_text = i.read()
        
    cipher = AES.new(key, AES.MODE_CBC)
    ini_vector = cipher.iv
    
    # padding data
    pad = 16 - len(plain_text) % 16
    plain_text_padded = plain_text + chr(pad) * pad
    
    # encrypt data
    cipher_text = cipher.encrypt(plain_text_padded.encode("utf-8"))
    result = base64.b64encode(ini_vector + cipher_text).decode("utf-8")
    
    # store result
    with open(output, "w", encoding="utf-8") as o:
        o.write(result)
    
    print(f"Email encrypted successfully!")
    
encrypt() 