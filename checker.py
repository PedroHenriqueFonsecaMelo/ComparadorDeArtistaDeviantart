import requests
import re
import time

# Nome do arquivo com os usuários
arquivo_usuarios = "users.txt"

# Lendo a lista de usuários do arquivo
with open(arquivo_usuarios, "r", encoding="utf-8") as f:
    usuarios = [linha.strip() for linha in f.readlines()]

# URL base do DeviantArt
url_base = "https://www.deviantart.com/"

# Listas para armazenar resultados
corretos = []
diferentes = []
nao_existentes = []
bloqueados = []

# Cabeçalhos HTTP para evitar bloqueio
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
}

print("\n🔍 Verificando usuários no DeviantArt (Case-Sensitive)...\n")

for usuario in usuarios:
    url = f"{url_base}{usuario}"

    try:
        response = requests.get(url, headers=headers, timeout=5)

        if response.status_code == 200:
            # Usamos regex para extrair o nome exato do atributo data-username
            match = re.search(r'data-username="(.*?)"', response.text)

            if match:
                nome_real = match.group(1)

                if nome_real == usuario:
                    corretos.append(usuario)
                    print(f"✅ Nome exato: {usuario}")
                else:
                    diferentes.append(f"{usuario} -> {nome_real}")
                    print(f"⚠ Nome diferente: {usuario} -> {nome_real}")

            else:
                print(f"⚠ Usuário {usuario} não encontrado, mas a página existe.")
                nao_existentes.append(f"{usuario} -> Página encontrada, mas sem nome.")

        elif response.status_code == 403:
            print(f"🚫 Bloqueado: {usuario} (Erro 403 - Request blocked)")
            bloqueados.append(usuario)

        else:
            trecho_html = response.text[:500]  # Captura um pedaço do HTML para análise
            print(f"❌ Não existe: {usuario} (HTML retornado: {trecho_html})")
            nao_existentes.append(f"{usuario} -> {trecho_html}")

    except requests.exceptions.RequestException as e:
        print(f"⚠ Erro ao verificar {usuario}: {e}")
        nao_existentes.append(f"{usuario} -> Erro de conexão")

    # Espera 30 segundos antes da próxima requisição
    print("⏳ Aguardando 30 segundos antes da próxima verificação...")
    time.sleep(30)

# Salvar resultados em arquivos de texto
with open("usuarios_corretos.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(corretos))

with open("usuarios_diferentes.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(diferentes))

with open("usuarios_nao_existentes.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(nao_existentes))

with open("usuarios_bloqueados.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(bloqueados))

print("\n✅ Verificação concluída!")
print(f"📂 Usuários com nome exato: {len(corretos)} (salvo em 'usuarios_corretos.txt')")
print(f"📂 Usuários com nome diferente: {len(diferentes)} (salvo em 'usuarios_diferentes.txt')")
print(f"📂 Usuários inexistentes: {len(nao_existentes)} (salvo em 'usuarios_nao_existentes.txt')")
print(f"📂 Usuários bloqueados: {len(bloqueados)} (salvo em 'usuarios_bloqueados.txt')")
