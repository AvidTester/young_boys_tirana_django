Project: Young Boys Tirana (Django)

Overview
-
This repo contains a small Django site that renders the existing static frontend (`assets/`) via a `core` app with models for site settings, team members, matches and pages.

Prerequisites
-
- Python 3.10+ installed
- Git (optional)

Quick start (Windows PowerShell)
-
1. Create and activate a virtual environment
```powershell
python -m venv env
.\env\Scripts\Activate.ps1
```

2. Install dependencies
```powershell
pip install -r requirements.txt
```

3. Apply migrations
```powershell
python manage.py migrate
```

4. Seed sample data
```powershell
python manage.py seed_data
```

5. Create an admin user
```powershell
python manage.py createsuperuser
```

6. Run the dev server
```powershell
python manage.py runserver
```

7. Open the admin
-
Visit: http://127.0.0.1:8000/admin and sign in with the superuser credentials.

Notes
-
- The project uses SQLite by default. The DB file is `db.sqlite3` in the project root.
- Static assets are served from the `assets/` folder (configured in `mysite/settings.py`).
- If `seed_data` fails, ensure migrations ran successfully (`python manage.py migrate`).

Adding content
-
Use the Django admin to edit site settings, create `TeamMember` and `Match` entries, or edit `PageContent`.

Files of interest
-
- [mysite/settings.py](mysite/settings.py) — Django settings (DB and static files)
- [core/models.py](core/models.py) — data models
- [core/management/commands/seed_data.py](core/management/commands/seed_data.py) — seed command

If you'd like, I can run `migrate` and `seed_data` here, or add a `requirements-dev.txt` and GitHub workflow for CI.

MySQL setup
-
If you prefer MySQL instead of the default SQLite, follow these steps.

1. Install a MySQL server (MySQL or MariaDB) and create a database and user. Example using the MySQL shell:
```sql
CREATE DATABASE youngboys_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'yuser'@'localhost' IDENTIFIED BY 'securepassword';
GRANT ALL PRIVILEGES ON youngboys_db.* TO 'yuser'@'localhost';
FLUSH PRIVILEGES;
```

2. Set environment variables (PowerShell example):
```powershell
$env:MYSQL_DATABASE = 'youngboys_db'
$env:MYSQL_USER = 'yuser'
$env:MYSQL_PASSWORD = 'securepassword'
$env:MYSQL_HOST = '127.0.0.1'
$env:MYSQL_PORT = '3306'
```

3. Install the Python MySQL adapter. This project uses `PyMySQL` (pure Python) by default; it's listed in `requirements.txt`.
```powershell
pip install -r requirements.txt
```

Note: `mysqlclient` is an alternative adapter (C extension) that is slightly faster but requires build tools on Windows; install it instead if you prefer.

4. Run migrations, seed data and start the server:
```powershell
python manage.py migrate
python manage.py seed_data
python manage.py createsuperuser
python manage.py runserver
```

If you run into adapter errors on Windows, try installing `mysqlclient` wheels from Christoph Gohlke's site or use the `PyMySQL` shim already included in `mysite/__init__.py`.