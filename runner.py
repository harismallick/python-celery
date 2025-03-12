import time
from tasks import add_nums, square_num, read_dir, read_file
from uuid import uuid4, UUID

# Runner test 1:
# results_promise: list = []

# for i in range(5):
#     # For celery to generate its own id for jobs:
#     # results_promise.append(add_nums.delay(1,2,3,4,5))
#     # Pass your own id for the job:
#     id: str = str(uuid4())
#     results_promise.append(add_nums.apply_async((1,2,3,4,5), task_id=id))
#     print(f"ID for task {i}: {id}")
#     id2: str = str(uuid4())
#     results_promise.append(square_num.apply_async([5], task_id=id2))


# for _ in range(10):
#     for i, result in enumerate(results_promise):
#         print(f"The sum for task {i}: {result.state}")
#     time.sleep(1)

# for result in results_promise:
#     print(result.get())
# print(type(results_promise[0]))

# Runner test 2:
# result: int = add_nums.apply_async((1,2,3,4,5), link=square_num.s(), countdown=10)
# print(result)

def path_runner(path: str) -> None:

    read_dir.apply_async([path], countdown=5)
    # if not is_file:
    #     print("Celery worker detected no file.")
    #     path_runner(path)
    
    # print("Celery worker detected files in given directory.")

    return



if __name__ == '__main__':
    
    path_runner("./test_dir")
    # path_runner("./test_dirdsak;lfjdlk;fjdask;fj")
    pass