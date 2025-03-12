import time
from celery import Celery
from maths import add_nums, square_num
from file_read import read_dir, read_file

# print("hello world")
app = Celery(
    "tasks", 
    broker="redis://localhost", 
    backend="db+postgresql://postgres:password@localhost:5433/postgres"
    )

app.task(add_nums)
app.task(square_num)
app.task(read_dir)
app.task(read_file)


if __name__ == '__main__':
    # sum = add_nums(1,2,3,4,5)
    # print(sum)
    pass