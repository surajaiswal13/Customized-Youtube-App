import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'custom_yt_api.settings')

app = Celery('custom_yt_api')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# Task scheduler
app.conf.beat_schedule = {
    'call_youtube_api': {
        'task': 'core.tasks.update_youtube_data',
        'schedule': 10
    },
}
