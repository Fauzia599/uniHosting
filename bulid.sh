set-0 errexit
pip install-r requiment.tx
python manage.py collectstatic --no-input
python manage.py migrate
if[[$SECEATE SUPERUSER]];
then python manage.py createsuperuser --no-input
fi