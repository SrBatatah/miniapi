# Mini API Flask — Módulo 1 (Organização e Versionamento)

Repositório público com uma mini API em **Flask**, organizada em `/src` e criada via **application factory** (`create_app`). O objetivo é evidenciar **organização do projeto** e **versionamento** com branches e commits padronizados.

---

## ✅ Entregáveis

- Estrutura organizada em `/src` com application factory.
- `requirements.txt` mínimo (runtime).
- `.gitignore` adequado para Python/venv/caches.
- README com execução (Windows e Linux/macOS), endpoints e exemplos.
- Histórico com branches e commits padronizados + PR no fluxo proposto.

---

## 📁 Estrutura

src/
init.py
app.py # create_app()
routes.py # rotas /users (GET, POST)
models.py # armazenamento em memória
config.py
.gitignore
requirements.txt
README.md

---

## 🧰 Requisitos

- Python 3.10+
- Flask (instalado via `pip`)

---

## ▶️ Como executar

### Windows (PowerShell)
```powershell
python -m venv .venv
& .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
flask --app src.app:create_app run --debug
