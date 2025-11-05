# Bank API - FastAPI Async (SQLite + JWT)

Projeto exemplo de uma API RESTful assíncrona construída com **FastAPI** para gerenciar
contas e transações bancárias (depósitos e saques). O projeto usa **SQLite** para
persistência e **JWT** para autenticação.

## Estrutura
```
bank-api/
├─ app/
│  ├─ __init__.py
│  ├─ main.py
│  ├─ config.py
│  ├─ db.py
│  ├─ models.py
│  ├─ schemas.py
│  ├─ crud.py
│  ├─ auth.py
│  └─ routers/
│     ├─ __init__.py
│     ├─ users.py
│     └─ accounts.py
├─ requirements.txt
└─ .env.example
```

## Como rodar (local, SQLite)

1. Crie e ative um virtualenv:

```bash
python -m venv venv
source venv/bin/activate   # mac/linux
venv\Scripts\activate    # windows
```

2. Instale dependências:
```bash
pip install -r requirements.txt
```

3. Copie `.env.example` para `.env` e ajuste `JWT_SECRET` se desejar.

4. Rode a aplicação:
```bash
uvicorn app.main:app --reload
```

5. Acesse a documentação interativa em `http://127.0.0.1:8000/docs`

## Notas
- Banco: SQLite (arquivo `bank.db` será criado no diretório do projeto).
- JWT: variável `JWT_SECRET` no `.env` ou em `app/config.py` (padrão para testes; troque em produção).
