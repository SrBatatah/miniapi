Mini API Flask — Organização e Versionamento
📌 Visão geral
Pequena API em Flask organizada em /src usando o padrão Application Factory (create_app). Layout simples, modular e fácil de evoluir.
________________________________________
🧰 Requisitos
•	Windows com Python 3.10+
•	Flask instalado via pip
•	Ambiente virtual com venv (recomendado)
________________________________________
🚀 Como executar (Windows • PowerShell)
python -m venv .venv
& .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
flask --app src.app:create_app run --debug
--debug liga o debugger e o reloader — use apenas em desenvolvimento.
________________________________________
📁 Estrutura do projeto
src/
  __init__.py
  app.py        # create_app()
  routes.py     # /users (GET, POST)
  models.py     # armazenamento em memória
  config.py
.gitignore
requirements.txt
README.md
________________________________________
🔗 Endpoints
•	GET /users — lista usuários (armazenados em memória).
•	POST /users — cria usuário. Body (JSON):
•	{ "name": "Nome", "email": "email@dominio.com" }
Resposta: 201 Created com { "id": <int> }.
Observação: existe também /health para verificação rápida do serviço.
________________________________________
🧪 Testes rápidos (Windows • PowerShell)
# listar
Invoke-RestMethod http://127.0.0.1:5000/users

# criar
$body = @{ name = "Ana"; email = "ana@email.com" } | ConvertTo-Json
Invoke-RestMethod -Method POST `
  -Uri http://127.0.0.1:5000/users `
  -Body $body -ContentType 'application/json'
________________________________________
🧭 Fluxo de trabalho (Git)
•	main — estável
•	develop — integração
•	feature/* — novas funcionalidades (a partir de develop)
git branch develop
git push -u origin develop

git checkout -b feature/usuarios develop
# ...implementar...
git add .
git commit -m "feat(users): implementar GET/POST"
git push -u origin feature/usuarios
# abrir PR: feature/usuarios -> develop
# depois PR: develop -> main
________________________________________
📝 Commits
Use mensagens claras e consistentes (ex.: feat(users): implementar GET/POST, fix(users): validar campos obrigatórios, docs(readme): incluir execução).
________________________________________
🙈 .gitignore (essencial)
.venv/
venv/
ENV/
__pycache__/
*.pyc
.DS_Store
📦 Dependências
Flask>=3.0
________________________________________
✅ Próximos passos
1.	Remover a seção antiga de referências do README (ou ao menos limpar os parâmetros utm_source=chatgpt.com dos links).
2.	Salvar o README acima.
3.	Commitar na branch feature/escopo-minimo (ou a sua atual) e abrir o PR para develop:
git add README.md
git commit -m "docs(readme): limpar referências e padronizar instruções"
git push
________________________________________
Fontes (para sustentar o padrão adotado)
•	Application Factory e execução via CLI no Flask. (Flask Documentation)
•	PowerShell Invoke-RestMethod (retorno JSON desserializado). (Microsoft Learn)
•	Template oficial Python.gitignore. (GitHub)

