# 🧠 CP3 - Pensamento Computacional com Python

Este projeto em Python reúne quatro exercícios com foco em manipulação de dados, uso de funções, estruturas de decisão, repetição e recursão. Os exercícios abordam desde o cadastro de produtos até criptografia, análise de texto e números perfeitos.

---

## 👨‍👩‍👧‍👦 Participante

- Raphael Taketa

---

## 🧾 Descrição dos Exercícios

### 🛒 Exercício 1 – Cadastro de Produtos com Estatísticas

Este módulo permite o cadastro de produtos com nome, preço e categoria, oferecendo estatísticas úteis com base nos dados inseridos.

📌 Funcionalidades:

- Cadastro ilimitado de produtos.
- Armazenamento em um dicionário no formato:
  produtos = {{
      "Produto1": {{"preco": 10.0, "categoria": "Alimento"}},
      ...
  }}
- Estatísticas exibidas:
  - Total de produtos cadastrados.
  - Média de preços por categoria.
  - Produto mais caro e mais barato.

---

### 🔐 Exercício 2 – Algoritmo de Criptografia Simples

Uma implementação da cifra de César usando dicionários para mapear letras com base em uma chave de deslocamento.

📌 Regras:

- Somente letras são criptografadas.
- Maiúsculas e minúsculas são preservadas.
- A criptografia é feita com a função:
  criptografar(texto: str, chave: int) -> str

🧪 Exemplo:

criptografar("Python é top!", 3) -> "Sbwkrq é wrs!"

---

### 🧠 Exercício 3 – Contador de Palavras Inteligente

Este módulo analisa um texto, contabilizando a frequência das palavras e retornando as 5 mais comuns.

📌 Funcionalidades:

- Remoção de pontuação.
- Contagem de frequência usando dicionário.
- Case-insensitive.
- Ignora palavras com menos de 3 letras.

Função principal:
analisar_texto(texto: str) -> dict

🧪 Exemplo de saída:
{'python': 8, 'dados': 6, 'função': 5, 'texto': 4, 'código': 3}

---

### 💯 Exercício 4 – Números Perfeitos com Recursão

Função que verifica se um número é perfeito usando recursão para somar divisores.

📌 Funcionalidades:

- Verificação com:
  eh_perfeito(n: int) -> bool
- Listagem de todos os números perfeitos até N:
  listar_perfeitos(N: int) -> list

🧪 Exemplo:
listar_perfeitos(1000) -> [6, 28, 496]

---


## 💻 Tecnologias Utilizadas

- Python
- Estruturas: dicionários, listas, funções, recursão, compreensão de listas
