from Crypto.Cipher import AES
import base64

def decrypt(input="emails/email_encrypted.txt",output="emails/email_decrypted.txt",key="keys/aes_key.key"):
    with open(key,"rb") as k:
        key=k.read()
        
    with open(input,"r",encoding="utf-8") as i:
        encoded_data = i.read()
        
    # convert data from base64 to binary
    data = base64.b64decode(encoded_data)
    init_vector = data[:16]
    cipher_text = data[16:]
    
    cipher = AES.new(key, AES.MODE_CBC, iv=init_vector)
    
    # decrypt and remove padding
    plain_text_padded = cipher.decrypt(cipher_text).decode("utf-8")
    pad = ord(plain_text_padded[-1])
    plain_text = plain_text_padded[:-pad]
    
    # store result
    with open(output, "w", encoding="utf-8") as o:
        o.write(plain_text)
        
    print(f"Email decrypted successfully")
    
decrypt()