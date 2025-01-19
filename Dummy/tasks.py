from celery import Celery


# Create a Celery instance
app = Celery('tasks', broker='pyamqp://guest@localhost//')


# Define a simple task
@app.task
def add(x, y):
    return x + y
