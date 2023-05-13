# Customized Youtube backend Using Youtube api

Customized Youtube for specific queries, it also keeps getting updated asynchronously

1. Create virtual environment
```
python -m venv venv
```

2. Activate virtual environment
```
venv\Sacript\actoiate
```
2. install all requirements
```
pip install requirements.txt
```

3. Migrate all changes to db
```
python manage.py migrate
```

3. Open Muliple command line terminal

4. Run django server
```
python manage.py runserver
```

5. Run celery
```
celery -A custom_yt_api worker -l INFO -P gevent
```

6. Run celery beat
```
celery -A custom_yt_api beat -l INFO
```

7. Access the api's
```
http://127.0.0.1:8000/youtube-data/
http://127.0.0.1:8000/search/
```

Thank you
