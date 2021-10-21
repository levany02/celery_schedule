import sys
sys.path.append("/home/default/ylv/celery/")

from flask import Flask
from task import make_celery

flask_app = Flask(__name__)
flask_app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_BACKEND='redis://localhost:6379'
)
celery = make_celery(flask_app)
celery.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'app.add_together',
        'schedule': 10.0,
        'args': (16, 16)
    },
}

@celery.task()
def add_together(a, b):
    print( a+ b)
    return a + b