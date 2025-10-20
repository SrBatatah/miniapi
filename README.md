# Mini API Flask — Organização e Versionamento

## 📌 Visão geral

Pequena API em **Flask** organizada em `/src` usando o padrão **Application Factory** (`create_app`). Layout simples, modular e fácil de evoluir.

---

## 🧰 Requisitos

* Windows com **Python 3.10+**
* **Flask** instalado via `pip`
* Ambiente virtual com `venv` (recomendado)

---

## 🚀 Como executar (Windows • PowerShell)

```powershell
python -m venv .venv
& .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
flask --app src.app:create_app run --debug
```

> `--debug` liga o *debugger* e o *reloader* — use apenas em desenvolvimento.

---

## 📁 Estrutura do projeto

```
src/
  __init__.py
  app.py        # create_app()
  routes.py     # /users (GET, POST)
  models.py     # armazenamento em memória
  config.py
.gitignore
requirements.txt
README.md
```

---

## 🔗 Endpoints

* **GET** `/users` — lista usuários (armazenados em memória).
* **POST** `/users` — cria usuário. **Body (JSON):**

  ```json
  { "name": "Nome", "email": "email@dominio.com" }
  ```

  **Resposta:** `201 Created` com `{ "id": <int> }`.

> Observação: existe também `/health` para verificação rápida do serviço.

---

## 🧪 Testes rápidos (Windows • PowerShell)

```powershell
# listar
Invoke-RestMethod http://127.0.0.1:5000/users

# criar
$body = @{ name = "Ana"; email = "ana@email.com" } | ConvertTo-Json
Invoke-RestMethod -Method POST `
  -Uri http://127.0.0.1:5000/users `
  -Body $body -ContentType 'application/json'
```

---

## 🧭 Fluxo de trabalho (Git)

* `main` — estável
* `develop` — integração
* `feature/*` — novas funcionalidades (a partir de `develop`)

```bash
git branch develop
git push -u origin develop

git checkout -b feature/usuarios develop
# ...implementar...
git add .
git commit -m "feat(users): implementar GET/POST"
git push -u origin feature/usuarios
# abrir PR: feature/usuarios -> develop
# depois PR: develop -> main
```

---

## 📝 Commits

Use mensagens claras e consistentes (ex.: `feat(users): implementar GET/POST`, `fix(users): validar campos obrigatórios`, `docs(readme): incluir execução`).

---

## 🙈 .gitignore (essencial)

```
.venv/
venv/
ENV/
__pycache__/
*.pyc
.DS_Store
```

## 📦 Dependências

```
Flask>=3.0
```

---

[1]: https://flask.palletsprojects.com/en/stable/patterns/appfactories/?utm_source=chatgpt.com "Application Factories — Flask Documentation (3.1.x)"
[2]: https://flask.palletsprojects.com/en/stable/server/?utm_source=chatgpt.com "Development Server — Flask Documentation (3.1.x)"
[3]: https://github.com/github/gitignore?utm_source=chatgpt.com "A collection of useful .gitignore templates"
[4]: https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore?utm_source=chatgpt.com "Python .gitignore - GitHub"
[5]: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/invoke-restmethod?view=powershell-7.5&utm_source=chatgpt.com "Invoke-RestMethod - PowerShell"
 
