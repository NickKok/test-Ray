import ray
from filelock import FileLock

@ray.remote
def write_to_file(text):
    # Create a filelock object. Consider using an absolute path for the lock.
    with FileLock('my_data.txt.lock'):
        with open('my_data.txt','a') as f:
            f.write(text)

ray.init()
ray.get([write_to_file.remote('hi there!\n') for i in range(3)])

with open('my_data.txt') as f:
    print(f.read())