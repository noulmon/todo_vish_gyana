release: python manage.py collectstatic --noinput && python manage.py migrate && python manage.py create_su
web: gunicorn todo_vish_gyana.wsgi:application
