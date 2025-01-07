import base64
import os
import re
from Crypto.Cipher import AES

def read_text_file(file_path, encoding="utf-8"):
    with open(file_path, "r", encoding=encoding, newline="") as f:
        return f.read()
    
def write_text_file(file_path, data, encoding="utf-8"):
    with open(file_path, "w", encoding=encoding, newline="") as f:
        f.write(data)
        
def read_binary_file(file_path):
    with open(file_path, "rb") as f:
        return f.read()
    
def write_binary_file(file_path, data):
    with open(file_path, "wb") as f:
        f.write(data)
        
def b64_encode(data):
    return base64.b64encode(data).decode("utf-8")

def b64_decode(encoded_string):
    return base64.b64decode(encoded_string)

def compute_email_size(file_path, block_size=AES.block_size, iv_size=16):
    file_size = os.path.getsize(file_path)
    padded_size = ((file_size + block_size - 1) // block_size) * block_size
    encrypted_size = iv_size + padded_size
    # Base64 encoding expands data by ~4/3
    base64_size = ((encrypted_size + 2) // 3) * 4
    return base64_size

def normalize_newlines(text: str) -> str:
    return re.sub(r'(\r\n|\r|\n)', '\n', text)