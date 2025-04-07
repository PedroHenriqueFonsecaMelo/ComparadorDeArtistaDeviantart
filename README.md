# ComparadorDeArtistaDeviantart
# **🔍 Verificador de Usuários no DeviantArt (Case-Sensitive)**  

Este script verifica a existência de usuários no **DeviantArt** a partir de um arquivo `.txt`, respeitando a diferenciação entre maiúsculas e minúsculas (**case-sensitive**).  

---

## 📄 **Descrição**  
O script acessa os perfis do DeviantArt e verifica:  
✅ Se o nome do usuário está correto (exatamente como digitado).  
⚠ Se o nome está diferente do esperado.  
❌ Se o usuário não existe.  
🚫 Se o acesso ao perfil foi bloqueado.  

Ao final, os resultados são salvos em arquivos `.txt`.  

---

## 📥 **Configuração**  

1. **Criar um arquivo de usuários** (`users.txt`) contendo um nome por linha:  
   ```
   UsuarioExemplo
   testeUser
   deviantArtist
   ```

2. **Executar o script** no terminal:  
   ```sh
   python verificar_usuarios.py
   ```

---

## 📤 **Saída do Script**  

Os resultados são armazenados nos seguintes arquivos:  

- `usuarios_corretos.txt` → Usuários encontrados com o nome exato.  
- `usuarios_diferentes.txt` → Usuários encontrados, mas com um nome diferente.  
- `usuarios_nao_existentes.txt` → Usuários inexistentes.  
- `usuarios_bloqueados.txt` → Perfis bloqueados (Erro 403).  

### 📌 **Exemplo de Saída no Terminal**  
```
✅ Nome exato: UsuarioExemplo  
⚠ Nome diferente: testeUser -> TesteUser  
❌ Não existe: deviantArtist  
⏳ Aguardando 30 segundos antes da próxima verificação...  
```

---

## 🛠 **Requisitos**  
- **Python 3+**  
- **Bibliotecas necessárias:**  
  - `requests`
  - `re`
  - `time`  

Se necessário, instale a biblioteca **requests** com:  
```sh
pip install requests
```

---

## 🔍 **Observações**  
- O script **espera 30 segundos** entre cada requisição para evitar bloqueios.  
- Caso um usuário tenha um nome diferente do esperado, o nome real será mostrado no terminal.  
- Se o DeviantArt bloquear a solicitação (Erro 403), o usuário será adicionado à lista de bloqueados.  

---

# **📁 Renomeador de Pastas (Case-Sensitive)**  

Este script renomeia pastas de acordo com uma lista fornecida em um arquivo `.txt`, garantindo que a diferenciação entre maiúsculas e minúsculas seja respeitada (**case-sensitive**).  

---

## 📄 **Descrição**  
O script lê um arquivo contendo os nomes das pastas antigas e os respectivos novos nomes, no formato:  
```
pastaAntiga -> PastaNova
teste -> Teste
exemplo -> Exemplo
```
Ele verifica se as pastas existem e realiza a renomeação de forma segura, garantindo que o Windows reconheça corretamente a mudança de letras maiúsculas e minúsculas.  

---

## 📥 **Configuração**  

1. **Criar um arquivo de nomes** (`usuarios_diferentes.txt`) com um nome por linha no formato:  
   ```
   yzaqtf -> YzaqTF
   testFolder -> TestFolder
   ```

2. **Definir os caminhos no script** (antes de rodar, edite o código e altere estas variáveis):  
   ```python
   base_path = r"C:\caminho\para\as\pastas"
   arquivo_usuarios = r"C:\caminho\para\usuarios_diferentes.txt"
   ```

3. **Executar o script** no terminal:  
   ```sh
   python renomear_pastas.py
   ```

---

## 📤 **Saída do Script**  

O script exibe mensagens no terminal indicando o progresso da renomeação:  

### 📌 **Exemplo de Saída no Terminal**  
```
✅ Renomeado: 'yzaqtf' -> 'YzaqTF' (Case-Sensitive)  
⚠ Pasta não encontrada: 'testFolder'. Pulando...  
✅ Renomeado: 'exemplo' -> 'Exemplo' (Case-Sensitive)  
✅ Processo concluído!  
```

---

## 🛠 **Requisitos**  
- **Python 3+**  

O script usa apenas a biblioteca **os** e **time**, que já vêm embutidas no Python, não sendo necessária nenhuma instalação adicional.  

---

## 🔍 **Observações**  
- O script **verifica se a pasta antiga existe** antes de tentar renomeá-la.  
- Para evitar problemas no Windows, quando os nomes diferem apenas em maiúsculas/minúsculas, o script usa um **renome temporário** antes da mudança final.  
- Se uma pasta informada no arquivo não existir, o script apenas exibe um aviso e continua.  

---

