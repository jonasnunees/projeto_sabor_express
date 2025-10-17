# 🍽️ Sabor Express (CLI)

Aplicativo de linha de comando (CLI) desenvolvido no curso da **Alura** para gerenciar um catálogo de restaurantes: cadastrar, listar, ativar/desativar e encerrar a aplicação.

> Projeto simples, didático e ideal para quem está começando em Python.

---

## ✨ Funcionalidades

- **Cadastrar restaurante** (nome e categoria)
- **Listar restaurantes** (com status Ativo/Inativo)
- **Ativar restaurante** (muda o status para ativo)
- **Desativar restaurante** (muda o status para inativo)
- **Interface de menu** com navegação simples
- **Finalizar aplicação**

---

## 🧱 Estrutura do projeto

```
.
└── app.py  # Código principal do aplicativo CLI
```

---

## 🛠️ Requisitos

- **Python 3.10+** (usa `match/case`)
- Sistema com suporte ao comando de limpar tela:
  - Windows: `cls` (usado via `os.system('cls')`)
  - (Opcional) Se for adaptar para Linux/macOS, troque por `clear`

---

## ▶️ Como executar

1. Garanta o Python 3.10+ instalado:
   ```bash
   python --version
   ```
2. Rode o aplicativo:
   ```bash
   python app.py
   ```
3. Use o **menu numérico** para navegar.

---

## 🖥️ Uso (exemplo de sessão)

```
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗...
1. Cadastrar restaurante
2. Listar restaurante
3. Ativar restaurante
4. Desativar restaurante
5. Sair

Escolha uma opção: 1
***********************
Cadastro de novos restaurantes
***********************

Digite o nome do restaurante que deseja cadastrar: Sabor Express
Digite a categoria do restaurante Sabor Express: Brasileira

O restaurante Sabor Express foi cadastrado com sucesso!

Digite uma tecla para voltar ao menu principal:
```

---

## 🧩 Como funciona (resumo técnico)

- A lista de restaurantes é mantida em memória como uma **lista de dicionários**:
  ```python
  restaurantes = [
    {"nome": "Menino do Açai", "categoria": "Hamburgueria", "ativo": True},
    ...
  ]
  ```
- O menu é mostrado em `exibir_menu()` e a navegação ocorre em `escolher_opcao()` usando `match/case`.
- Cada ação (cadastrar, listar, ativar, desativar) tem **sua própria função**.
- `voltar_ao_menu_principal()` pede uma tecla e chama `main()` para retornar ao menu.
- `exibir_subtitulo(texto)` limpa a tela e mostra um cabeçalho estilizado.
- `main()` orquestra a execução: limpa tela → cabeçalho → menu → leitura de opção.

---

## 🧪 Comportamentos importantes

- **Ativar/Desativar**: Busca pelo nome digitado; se não encontrar, informa ao usuário.
- **Tratamento de entrada inválida**: `escolher_opcao()` encapsula o input em `try/except` e chama `opcao_invalida()` se não for um número.
- **Limpar tela**: Feito com `os.system('cls')` (Windows). Para Linux/macOS, substitua por `clear`.

---

## 🚀 Executando em outros sistemas

Se estiver em Linux/macOS, uma adaptação comum é alterar:

```python
# Em exibir_subtitulo() e main():
os.system('cls')  # Windows
# para
os.system('clear')  # Linux/macOS
```

Ou criar um helper:

```python
import os, platform

def limpar_tela():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
```

---

## 🧷 Referência do código

- Arquivo principal: `app.py` — contém todas as funções e o fluxo do app.

---

## 📝 Licença

- Este projeto está licenciado sob a GNU General Public License v3.0 - veja o arquivo LICENSE para detalhes.

---

## 🙌 Agradecimentos

- Alura, pelo material e proposta do projeto.
- Comunidade Python.
