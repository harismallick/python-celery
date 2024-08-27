import time
from tasks import add_nums
from uuid import uuid4, UUID

results_promise: list = []

for i in range(5):
    # For celery to generate its own id for jobs:
    # results_promise.append(add_nums.delay(1,2,3,4,5))
    # Pass your own id for the job:
    id: str = str(uuid4())
    results_promise.append(add_nums.apply_async((1,2,3,4,5), task_id=id))
    print(f"ID for task {i}: {id}")


for _ in range(10):
    for i, result in enumerate(results_promise):
        print(f"The sum for task {i}: {result.state}")
    time.sleep(1)

for result in results_promise:
    print(result.get())
print(type(results_promise[0]))