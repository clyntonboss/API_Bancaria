# 💰 API Bancária Assíncrona com FastAPI

![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Asynchronous-green)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)
![JWT](https://img.shields.io/badge/Auth-JWT-orange)
![License](https://img.shields.io/badge/License-MIT-lightblue)

---

## 🧠 Sobre o Projeto

O **Desafio: API Bancária Assíncrona com FastAPI** foi desenvolvido como parte do curso:

> **Certificação:** Luizalabs – Dominando Funções e Boas Práticas em Python™  
> **Curso:** Criando sua API Bancária Assíncrona com FastAPI™  
> **Módulo:** Evoluindo com APIs Assíncronas com FastAPI™

Esta aplicação tem como objetivo demonstrar a criação de uma **API RESTful** moderna, segura e eficiente, utilizando **FastAPI** com operações **assíncronas**, **autenticação JWT** e persistência de dados em **SQLite**.

A API foi projetada para gerenciar **contas bancárias**, **transações (depósitos e saques)** e **consultas de extratos**, aplicando boas práticas de arquitetura, modularização e segurança.

---

## ⚙️ Funcionalidades

✅ Cadastro de usuários e autenticação com JWT  
✅ Criação de contas bancárias  
✅ Registro de transações (depósito e saque)  
✅ Validação de saldo e valores negativos  
✅ Consulta de extrato completo da conta  
✅ Documentação interativa via Swagger (OpenAPI)  
✅ Banco de dados local em SQLite  

---

## 🧩 Estrutura do Projeto

```bash
📂 app/
├── __init__.py
├── main.py                # Ponto de entrada da aplicação
├── database.py            # Conexão e inicialização do banco SQLite
├── models.py              # Modelos ORM (SQLAlchemy)
├── schemas.py             # Estruturas Pydantic para validação de dados
├── auth.py                # Lógica de autenticação e geração de tokens JWT
├── routers/
│   ├── users.py           # Endpoints de usuários e autenticação
│   ├── accounts.py        # Endpoints de contas bancárias
│   └── transactions.py    # Endpoints de transações
├── utils/
│   └── security.py        # Funções auxiliares para criptografia e validações
├── .env.example           # Exemplo de variáveis de ambiente
├── requirements.txt       # Dependências do projeto
└── README.md              # Documentação do projeto

# 🚀 Como Executar o Projeto
1️⃣ Clonar o repositório

git clone https://github.com/SEU_USUARIO/bank-api.git
cd bank-api

2️⃣ Criar ambiente virtual e instalar dependências

python -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows

pip install -r requirements.txt

3️⃣ Executar a API

uvicorn app.main:app --reload

4️⃣ Acessar a documentação interativa

    Swagger UI: http://127.0.0.1:8000/docs

Redoc: http://127.0.0.1:8000/redoc
🔐 Autenticação JWT

A API utiliza JSON Web Token (JWT) para proteger endpoints sensíveis.
Exemplo de fluxo:

    Crie um usuário (POST /users/register)

    Faça login (POST /users/login) e receba o token JWT

    Envie o token no header Authorization: Bearer <token> para acessar endpoints protegidos

🧾 Exemplos de Requisições
🔸 Criar Usuário

POST /users/register
{
  "username": "chronos",
  "password": "123456"
}

🔸 Login

POST /users/login
{
  "username": "chronos",
  "password": "123456"
}

🔸 Criar Conta

POST /accounts/
{
  "user_id": 1
}

🔸 Realizar Depósito

POST /transactions/deposit
{
  "account_id": 1,
  "amount": 500.00
}

🔸 Realizar Saque

POST /transactions/withdraw
{
  "account_id": 1,
  "amount": 100.00
}

🔸 Consultar Extrato

GET /accounts/1/statement
Authorization: Bearer <token>

🧭 Endpoints Principais
Método	Endpoint	Descrição	Autenticação
🟩 POST	/users/register	Cadastra um novo usuário	❌
🟩 POST	/users/login	Autentica o usuário e gera token JWT	❌
🟩 POST	/accounts/	Cria uma conta para o usuário autenticado	✅
🟦 GET	/accounts/{id}/statement	Retorna o extrato da conta	✅
🟨 POST	/transactions/deposit	Realiza um depósito na conta	✅
🟥 POST	/transactions/withdraw	Realiza um saque na conta (se houver saldo)	✅
🛡️ Validações Implementadas

    ❌ Bloqueio de transações com valores negativos

    ⚖️ Verificação de saldo antes de permitir saques

    🔐 Proteção de endpoints com autenticação JWT

    🧱 Associação entre conta e usuário

🧠 Tecnologias Utilizadas
Categoria	Ferramenta
Linguagem	Python 3.10+
Framework	FastAPI
Banco de Dados	SQLite
ORM	SQLAlchemy
Autenticação	JWT (PyJWT)
Validação	Pydantic
Servidor	Uvicorn
🧩 Boas Práticas Implementadas

    Organização modular seguindo arquitetura limpa

    Uso de async/await para operações assíncronas

    Separação entre camadas (Models, Schemas, Routers e Utils)

    Documentação automática com OpenAPI / Swagger

    Tratamento de exceções e respostas padronizadas

🧪 Testes e Validação

Os endpoints podem ser testados diretamente via Swagger UI ou ferramentas como Postman e Insomnia.
Todos os métodos possuem validações de entrada via Pydantic, garantindo integridade e consistência dos dados.
📦 Requisitos

    Python 3.10 ou superior

    pip atualizado

    FastAPI, Uvicorn, SQLAlchemy, PyJWT e Pydantic

Instale tudo com:

pip install -r requirements.txt

📜 Licença

Este projeto está sob a licença MIT.
Sinta-se livre para utilizá-lo, modificá-lo e aprimorá-lo conforme suas necessidades.
👨‍💻 Autor

Rogério Clynton Ribeiro
💼 ClyntonBoss


💡 “Inovação é transformar conhecimento em valor real.”
💬 Agradecimentos

Agradecimentos especiais à equipe Luizalabs e DIO (Digital Innovation One) pela inspiração e incentivo ao domínio de boas práticas em Python™ e desenvolvimento assíncrono com FastAPI.

⭐ Se este projeto te inspirou, não esqueça de deixar uma estrela no repositório!
