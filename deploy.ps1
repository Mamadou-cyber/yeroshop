$ErrorActionPreference = "Stop"

# Remplacez "poetry" par l'appel via Python
python -m poetry install --no-interaction --no-ansi
python manage.py collectstatic --noinput --clear
python manage.py migrate --noinput