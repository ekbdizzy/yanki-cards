until ./manage.py migrate
do
    echo "Waiting for DB"
    sleep 2
done

./manage.py collectstatic --noinput
gunicorn server.wsgi --bind 0.0.0.0:8000
