import ray
import time

ray.init()
# ray.init(num_cpus=8, num_gpus=4, resources={'Custom': 2})


@ray.remote(num_cpus=4, num_gpus=1)
def my_function():
    return 1


@ray.remote
def function_with_an_argument(value):
    return value + 1

obj_ref1 = my_function.remote()
assert ray.get(obj_ref1) == 1
print( ray.get(obj_ref1))

# You can pass an object ref as an argument to another Ray remote function.
obj_ref2 = function_with_an_argument.remote(obj_ref1)
assert ray.get(obj_ref2) == 2 
print( ray.get(obj_ref2))

@ray.remote(num_returns=3)
def return_function():
    return 1, 2, 3


a, b, c = ray.get(return_function.remote())
print(a, b, c)



@ray.remote
def blocking_operation():
    time.sleep(10e6)

obj_ref = blocking_operation.remote()
ray.cancel(obj_ref)

from ray.exceptions import TaskCancelledError

try:
    ray.get(obj_ref)
except TaskCancelledError:
    print("Object reference was canceled")


y = 12
object_ref12 = ray.put(y)


assert  ray.get(object_ref12) == 12

# Get the values of multiple object refs in parallel.
assert ray.get([ray.put(i) for i in range(3)]) == [0, 1, 2]

# You can also set a timeout to return early from a ``get`` that's blocking for too long.
from ray.exceptions import GetTimeoutError

@ray.remote
def long_running_operation():
    time.sleep(8)

obj_ref = long_running_operation.remote()

try:
    ray.get(obj_ref, timeout=4)
except GetTimeoutError:
    print('get timed out')




