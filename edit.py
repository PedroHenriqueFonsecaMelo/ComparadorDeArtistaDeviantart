import os
import time

# Definir os caminhos
base_path = r""
arquivo_usuarios = r""

# Verificar se o arquivo de nomes existe
if not os.path.exists(arquivo_usuarios):
    print(f"❌ Arquivo não encontrado: {arquivo_usuarios}")
    exit()

# Ler os nomes do arquivo
with open(arquivo_usuarios, "r", encoding="utf-8") as file:
    linhas = file.readlines()

# Processar cada linha do arquivo
for linha in linhas:
    linha = linha.strip()
    if " -> " in linha:  # Verifica se está no formato correto
        antigo, novo = linha.split(" -> ")
        caminho_antigo = os.path.join(base_path, antigo)
        caminho_novo = os.path.join(base_path, novo)

        # Verifica se a pasta antiga existe
        if os.path.exists(caminho_antigo) and os.path.isdir(caminho_antigo):
            # Se os nomes diferem apenas em maiúsculas/minúsculas, faz a renomeação em dois passos
            if antigo.lower() == novo.lower():
                temp_path = os.path.join(base_path, f"TEMP_RENAME_{int(time.time())}")  # Nome temporário único
                os.rename(caminho_antigo, temp_path)
                time.sleep(1)  # Aguarda 1 segundo para garantir que o Windows processe a mudança
                os.rename(temp_path, caminho_novo)
            else:
                os.rename(caminho_antigo, caminho_novo)
            
            print(f"✅ Renomeado: '{antigo}' -> '{novo}' (Case-Sensitive)")
        else:
            print(f"⚠ Pasta não encontrada: '{antigo}'. Pulando...")

print("✅ Processo concluído!")
