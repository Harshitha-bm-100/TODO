# Todos

Keep a task list in a SQLite database and manage it in the browser.

## Description

Todos is a small Django web app for a task list. On the home page you type a task and press Add. Django writes one row to a local SQLite database. The same page lists every task. Open tasks come first, and within each group the newest task is first. The heading shows how many tasks are still open. Click the box beside a task to mark it complete or open again. Press Delete to remove that row. A missing id shows a 404 page. The same records are also available in Django admin after you create an admin login.

The title is required and can be up to 200 characters. A blank title is ignored. Completed and the created time are set by Django.

## Getting Started

### Dependencies

- Python 3
- pip
- Git

Django 6.1.2 is installed from `requirements.txt`. SQLite comes with Python, so you do not install a separate database. The app runs on macOS, Linux, and Windows.

### Installing

Open a terminal in this folder and install the dependencies inside a virtual environment.

macOS and Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
```

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
```

`migrate` creates `db.sqlite3` in the project folder and the `todos_todo` table. That file is local. It is listed in `.gitignore`. No project files need to be edited before the first run. Install the requirements once per virtual environment, not on every start.

### Executing program

1. Activate the virtual environment if the terminal does not already show `(.venv)`.
2. Start the server:

```bash
python manage.py runserver
```

3. Open http://127.0.0.1:8000/.
4. Type a task and press Add.
5. Click the box beside a task to complete it, or press Delete to remove it.

Optional admin site:

```bash
python manage.py createsuperuser
```

Then open http://127.0.0.1:8000/admin/ and sign in with that account.

Stop the server with Ctrl+C.

## Authors

- [Harshitha-bm-100](https://github.com/Harshitha-bm-100)

## Version History

- 0.1
  - Initial release
