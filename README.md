# Mini API Flask — Organização e Versionamento

## 📌 Visão geral

Pequena API em **Flask** organizada em `/src` usando o padrão **Application Factory** (`create_app`). Layout pensado para ser simples, modular e fácil de evoluir. ([Flask Documentation][1])

---

## 🧰 Requisitos

* Windows com **Python 3.10+**
* **Flask** instalado via `pip`
* Ambiente virtual com `venv` (recomendado)
* Execução via **Flask CLI** com `--app` e `--debug` (apenas em desenvolvimento). ([Flask Documentation][2])

---

## 🚀 Como executar (Windows • PowerShell)

```powershell
python -m venv .venv
& .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
flask --app src.app:create_app run --debug
```

> `--debug` liga o *debugger* e o *reloader* — **nunca** use isso em produção. ([Flask Documentation][3])

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

> Padrão “aplicação como pacote” + factory facilita testes, blueprints e extensões. ([Flask Documentation][4])

---

## 🔗 Endpoints

* **GET** `/users` — lista usuários (armazenados em memória).
* **POST** `/users` — cria usuário. **Body (JSON):**

  ```json
  { "name": "Nome", "email": "email@dominio.com" }
  ```

  **Resposta:** `201 Created` com `{ "id": <int> }`.

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

> `Invoke-RestMethod` converte JSON da resposta em objetos PowerShell automaticamente. ([Microsoft Learn][5])

---

## 🧭 Fluxo de trabalho sugerido (Git)

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

> Baseado no template oficial **Python.gitignore** do GitHub. ([GitHub][6])

---

## 📦 Dependências

```
Flask>=3.0
```

---

## 📚 Referências

* Flask — **Application Factory** e padrões. ([Flask Documentation][1])
* Flask CLI — `--app` e `--debug` (desenvolvimento). ([Flask Documentation][2])
* PowerShell — `Invoke-RestMethod` com JSON. ([Microsoft Learn][5])
* GitHub — **Python.gitignore**. ([GitHub][6])

> Pronto para colar no seu README. Se quiser, eu adapto o texto para o tom da sua equipe (mais formal/curto) ou incluo badges e seções extras (ex.: Roadmap, Contribuição, Licença).

[1]: https://flask.palletsprojects.com/en/stable/patterns/appfactories/?utm_source=chatgpt.com "Application Factories — Flask Documentation (3.1.x)"
[2]: https://flask.palletsprojects.com/en/stable/cli/?utm_source=chatgpt.com "Command Line Interface — Flask Documentation (3.1.x)"
[3]: https://flask.palletsprojects.com/en/stable/debugging/?utm_source=chatgpt.com "Debugging Application Errors — Flask Documentation (3.1.x)"
[4]: https://flask.palletsprojects.com/en/stable/patterns/?utm_source=chatgpt.com "Patterns for Flask — Flask Documentation (3.1.x)"
[5]: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/invoke-restmethod?view=powershell-7.5&utm_source=chatgpt.com "Invoke-RestMethod - PowerShell"
[6]: https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore?utm_source=chatgpt.com "Python .gitignore - GitHub"
