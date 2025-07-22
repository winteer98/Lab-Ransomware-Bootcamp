import os
import pyaes

def decrypt_file(encrypted_path, key):
    with open(encrypted_path, 'rb') as f:
        encrypted_data = f.read()

    aes = pyaes.AESModeOfOperationCTR(key)
    decrypted_data = aes.decrypt(encrypted_data)

    os.remove(encrypted_path)

    original_path = encrypted_path.replace(".ransomwaretroll", "")
    with open(original_path, 'wb') as f:
        f.write(decrypted_data)

    print(f"Arquivo descriptografado: {original_path}")

if __name__ == "__main__":
    decrypt_file("teste.txt.ransomwaretroll", b"testeransomwares")
