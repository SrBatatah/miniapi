# Mini API Flask — Módulo 1 (Organização e Versionamento)

Repositório público com uma mini API em Flask, organizada em /src e criada via application factory (create_app). Objetivo: demonstrar organização do projeto e versionamento com branches e commits padronizados.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📁 ESTRUTURA DO PROJETO

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

src/
  __init__.py
  app.py        # create_app()
  routes.py     # rotas /users (GET, POST)
  models.py     # armazenamento em memória
  config.py
.gitignore
requirements.txt
README.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🧰 REQUISITOS

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Windows com Python 3.10+ instalado
- Flask (instalado via pip)
- Recomenda-se usar ambiente virtual (venv)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

▶️ COMO EXECUTAR (WINDOWS • POWERSHELL)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1) Criar e ativar a venv
   python -m venv .venv
   & .\.venv\Scripts\Activate.ps1

2) Instalar dependências
   pip install -r requirements.txt

3) Rodar a aplicação (servidor de desenvolvimento)
   flask --app src.app:create_app run --debug

Obs.: --debug ativa recarregamento automático e debugger (apenas em desenvolvimento).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔗 ENDPOINTS

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- GET /users
  → Lista usuários (armazenamento em memória).

- POST /users
  → Cria um usuário.
  Body (JSON):
    { "name": "Ana", "email": "ana@email.com" }
  Resposta:
    201 Created
    Corpo: { "id": <int> }

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🧪 EXEMPLOS (WINDOWS • POWERSHELL)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# listar
Invoke-RestMethod http://127.0.0.1:5000/users

# criar
$body = @{ name = "Ana"; email = "ana@email.com" } | ConvertTo-Json
Invoke-RestMethod -Method POST `
  -Uri http://127.0.0.1:5000/users `
  -Body $body -ContentType 'application/json'

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🧭 FLUXO DE VERSIONAMENTO (GIT FLOW SIMPLIFICADO)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Branches:
- main      → estável (entrega)
- develop   → integração
- feature/* → novas funcionalidades (saem de develop)

Roteiro (linha de comando):
# criar branch de integração (se ainda não existir)
git branch develop
git push -u origin develop

# nova feature
git checkout -b feature/usuarios develop
# ...implementar...
git add .
git commit -m "feat(users): implementar GET/POST"
git push -u origin feature/usuarios

# abrir PR: feature/usuarios -> develop
# após revisar/mesclar, abrir PR: develop -> main

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 PADRÃO DE COMMITS (CONVENTIONAL COMMITS)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Formato:
<type>(scope): <description>

Exemplos:
- feat(users): implementar GET/POST
- fix(users): validar campos obrigatórios
- docs(readme): incluir instruções de execução

Tipos comuns: feat, fix, docs, test, chore, refactor.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🙈 .GITIGNORE (RESUMO)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# ambientes virtuais
.venv/
venv/
ENV/

# caches python
__pycache__/
*.pyc

# pacotes locais/offline
vendor/

# arquivos de SO/editor
.DS_Store

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📦 DEPENDÊNCIAS

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
