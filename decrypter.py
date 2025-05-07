import os
import pyaes

# Nome do arquivo criptografado
file_name = "arquivo.txt.ransomwaresim"

# Verifica se o arquivo existe
if not os.path.exists(file_name):
    print(f"Arquivo '{file_name}' não encontrado.")
    exit()

# Abrir e ler o conteúdo do arquivo criptografado
with open(file_name, "rb") as file:
    file_data = file.read()

# Chave de descriptografia (deve ser igual à usada na criptografia)
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

# Descriptografar os dados
decrypt_data = aes.decrypt(file_data)

# Remover o arquivo criptografado
os.remove(file_name)

# Nome do arquivo restaurado
new_file = "teste.txt"

# Criar o novo arquivo descriptografado
with open(new_file, "wb") as file:
    file.write(decrypt_data)

print(f"Arquivo '{new_file}' restaurado com sucesso.")
