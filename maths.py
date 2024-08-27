import time
from celery import shared_task

@shared_task
def add_nums(*nums) -> int:
    sum: int = 0

    for i in nums:
        sum += i
    time.sleep(5)
    return sum
