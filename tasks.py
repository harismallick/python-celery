import time
from celery import Celery
from maths import add_nums

print("hello world")
app = Celery(
    "tasks", 
    broker="redis://localhost", 
    backend="db+postgresql://postgres:password@localhost:5433/postgres"
    )

app.task(add_nums)


if __name__ == '__main__':
    # sum = add_nums(1,2,3,4,5)
    # print(sum)
    pass