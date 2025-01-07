import os
from src.encrypt_email import encrypt
from src.decrypt_email import decrypt
from src.utils import read_binary_file

def test(input_file,encrypt_file="data/email_encrypted.txt",decrypt_file="data/email_decrypted.txt",log_file="results/test_results.log"):
    try:
        original_data = read_binary_file(input_file)
    except FileNotFoundError:
        print(f"Test {os.path.basename(input_file)}: ERROR (file not found)")
        return

    encrypt(input_file, encrypt_file)
    decrypt(encrypt_file, decrypt_file)

    try:
        decrypted_data = read_binary_file(decrypt_file)
    except Exception as e:
        print(f"Error reading decrypted binary file: {decrypt_file}\n{str(e)}")
        return
    
    result = "PASS" if original_data == decrypted_data else "FAIL"
    try:
        original_size = len(original_data)
        encrypted_size = os.path.getsize(encrypt_file)

        with open(log_file, "a", encoding="utf-8") as log:
            log.write(f"Test File: {os.path.basename(input_file)}\n")
            log.write(f"Result: {result}\n")
            log.write(f"Original Size: {original_size} bytes\n")
            log.write(f"Encrypted Size: {encrypted_size} bytes\n\n")

        print(f"Test {os.path.basename(input_file)}: {result}\n\n")

    except Exception as e:
        with open(log_file, "a", encoding="utf-8") as log:
            log.write(f"Test File: {os.path.basename(input_file)}\n")
            log.write(f"Error: {str(e)}\n\n")
        print(f"Test {os.path.basename(input_file)}: ERROR")


if __name__ == "__main__":
    test_cases = [
        "tests/test_long_email.txt",
        "tests/test_short_email.txt",
        "tests/test_unicode_email.txt",
        "tests/email_pdf.pdf"
    ]

    for test_case in test_cases:
        test(
            input_file=test_case,
            encrypt_file="data/email_encrypted.txt",
            decrypt_file="data/email_decrypted.txt",
            log_file="results/test_results.log"
        )
