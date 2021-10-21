from celery import Celery
from celery.schedules import crontab

app = Celery('schedule_tasksx', backend='redis://localhost', broker='redis://localhost')

# app.conf.beat_schedule = {
#     'add-every-30-seconds': {
#         'task': 'schedule_tasks.add',
#         'schedule': 30.0,
#         'args': (16, 16)
#     },
# }
app.conf.timezone = 'UTC'

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    # sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')
    sender.add_periodic_task(2.0, add.s(15, 45), name='add every 10')

    # Calls test('world') every 30 seconds
    # sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    # sender.add_periodic_task(
    #     crontab(hour=7, minute=30, day_of_week=1),
    #     test.s('Happy Mondays!'),
    # )


@app.task
def test(arg):
    print(arg)


@app.task
def add(x, y):
    z = x + y
    print(z)