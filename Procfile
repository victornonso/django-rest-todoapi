# web: gunicorn todolistapi.wsgi

web: waitress-serve --port=$PORT todolistapi.wsgi:application
release: python manage.py makemigrations --noinput
release: python manage.py collectstatic --noinput
release: python manage.py migrate --noinput
