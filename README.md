# Esquema Criptográfico Simplificado em Python

Este projeto consiste na implementação de um **esquema criptográfico simplificado**, desenvolvido como parte da disciplina de **Segurança / Criptografia**.  
O objetivo é aplicar conceitos fundamentais de **geração de chaves**, **cifragem** e **avaliação de qualidade de cifras** (Difusão e Confusão), utilizando a linguagem **Python 3.10**.

---

## 📋 Especificação do Trabalho

O sistema é composto por três funções principais obrigatórias:

- **GEN (Key Generation):**  
  Recebe uma semente (`seed`) e gera uma **chave binária** de comprimento fixo.

- **ENC (Encryption):**  
  Recebe a **chave** e a **mensagem** (ambas binárias e de mesmo tamanho) e retorna a **cifra**.

- **DEC (Decryption):**  
  Recebe a **chave** e a **cifra**, retornando a **mensagem original**.

---

## 🛠️ Implementação Técnica

A implementação utiliza recursos nativos da linguagem Python para atender aos critérios de segurança exigidos:

- **Geração de Chaves:**  
  Utiliza a biblioteca `hashlib` com o algoritmo **SHA-256**, garantindo alta dependência da chave em relação à semente e minimizando a possibilidade de **chaves equivalentes**.

- **Cifragem e Descriptografia:**  
  Baseadas na operação lógica **XOR**, que apresenta:
  - Simplicidade de implementação  
  - Eficiência computacional  
  - Reversibilidade matemática (ENC e DEC utilizam a mesma operação)

---

## 🧪 Testes de Qualidade

O código inclui testes automatizados para validar os critérios exigidos pelo trabalho.

### 1. Teste de Difusão

Avalia quantos bits da cifra são alterados quando **apenas 1 bit da mensagem** é modificado, mantendo a chave constante.  
No método XOR, a difusão ocorre de forma direta, bit a bit.

### 2. Teste de Confusão

Avalia o impacto da modificação de **1 único bit na semente (`seed`)** utilizada para gerar a chave.  
A mensagem permanece fixa, e observa-se a variação da cifra.  
Graças ao uso do **SHA-256**, uma pequena alteração na semente resulta em uma chave — e consequentemente uma cifra — completamente diferente.

---

## 🚀 Como Executar

1. Certifique-se de ter o **Python 3.10** instalado.

2. Clone este repositório:
   ```bash
   git clone git@github.com:Klaria-Data/auditoria_seguranca_criptografia_simplificada.git

3. Navegue até o diretório do projeto e execute:
    ```bash
    python main.py
