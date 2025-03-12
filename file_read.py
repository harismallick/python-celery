import time
import os
from celery import shared_task

@shared_task
def read_dir(path) -> None:

    files: list[str] = os.listdir(path)
    if len(files) == 0:
        print("No files in directory.")
        read_dir.apply_async([path], countdown=5)
        return
    
    for file in files:
        read_file.apply_async([f"{path}/{file}"])
    return

@shared_task
def read_file(path: str) -> None:
    time.sleep(1)
    with open(path, 'r') as file:
        for line in file:
            print(line)
    return

if __name__ == '__main__':
    read_dir("./test_dir")