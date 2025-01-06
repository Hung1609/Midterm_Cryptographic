import os
from src.encrypt_email import encrypt
from src.decrypt_email import decrypt

def test(input_file, encrypt_file, decrypt_file, log_file):
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            original_content = f.read()
            
        encrypt(input_file, encrypt_file)
        decrypt(encrypt_file, decrypt_file)
        
        with open(decrypt_file, "r", encoding="utf-8") as f:
            decrypt_content = f.read()
            
        result = "PASS" if original_content == decrypt_content else "FAIL"
        
        with open(log_file, "a", encoding="utf-8") as log:
            log.write(f"Test File: {os.path.basename(input_file)}\n")
            log.write(f"Result: {result}\n")
            log.write(f"Original Size: {len(original_content.encode('utf-8'))} bytes\n")
            log.write(f"Encrypted Size: {os.path.getsize(encrypt_file)} bytes\n")
            log.write("\n")
            
        print(f"Test {os.path.basename(input_file)}: {result}")
    except Exception as e:
        with open(log_file, "a", encoding="utf-8") as log:
            log.write(f"Test File: {os.path.basename(input_file)}\n")
            log.write(f"Error: {str(e)}\n")
            log.write("\n")
        print(f"Test {os.path.basename(input_file)}: ERROR")
        
        
if __name__ == "__main__":
    test_cases = [
        "tests/test_short_email.txt",
        "tests/test_long_email.txt",
        "tests/test_unicode_email.txt"
    ]
    for test_case in test_cases:
        test(
            input_file=test_case,
            encrypt_file="data/email_encrypted.txt",
            decrypt_file="data/email_decrypted.txt",
            log_file="results/test_results.log"
        )