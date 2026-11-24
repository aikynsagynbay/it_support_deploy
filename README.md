# IT-қолдау өтінімдерін тіркеу жүйесі (Lab 12: Deploy & Logging)

Django негізінде жасалған IT-қолдау өтінімдерін тіркеу, күйін бақылау және оқиғаларды журналға (INFO / WARNING) жазу жүйесі.

## Жергілікті іске қосу (PyCharm 2025.3.3)

1. Жобаны PyCharm-да ашып, виртуалды ортаны (`.venv`) құрыңыз.
2. Тәуелділіктерді орнатыңыз:
   ```bash
   pip install -r requirements.txt
   ```
3. Миграцияларды қолданып, серверді іске қосыңыз:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```
4. Браузерде `http://127.0.0.1:8000/` мекенжайын ашыңыз.

## Render бұлтына жариялау (Deploy)

- **Runtime:** `Python 3`
- **Build Command:** `bash build.sh`
- **Start Command:** `gunicorn config.wsgi:application --bind 0.0.0.0:$PORT`
- **Environment Variables:** `SECRET_KEY`, `DEBUG=False`, `ALLOWED_HOSTS`, `DATABASE_URL`
