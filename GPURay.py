import os
import numpy as np
import ray
import sqlite3
import threading


ray.init()


@ray.remote(num_gpus=1)
def use_gpu():
    print('ray.get_gpu_ids(): {}'.format(ray.get_gpu_ids()))
    print('Cuda_Visible_device: {}'.format(os.environ['CUDA_VISIBLE_DEVICES']))

obje = use_gpu.remote()


obj = [np.zeros(42)] * 99
l = ray.get(ray.put(obj))
print(l[0], l[1])

class DBConnection:
    def __init__(self, path):
        self.path = path
        self.conn = sqlite3.connect(path)

    # without '__reduce__', the instance is unserializable.
    def __reduce__(self):
        deserializer = DBConnection
        serialized_data = (self.path,)
        return deserializer, serialized_data

original = DBConnection("/tmp/db")
print(original.conn)

copied = ray.get(ray.put(original))
print(copied.conn)

class A:
    def __init__(self, x):
        self.x = x
        self.lock = threading.Lock()  # could not be serialized!

#ray.get(ray.put(A(1)))  # fail!

def custom_serializer(a):
    return a.x

def custom_deserializer(b):
    return A(b)

# Register serializer and deserializer for class A:
ray.util.register_serializer(
  A, serializer=custom_serializer, deserializer=custom_deserializer)
ray.get(ray.put(A(1)))  # success!

# You can deregister the serializer at any time.
ray.util.deregister_serializer(A)
ray.get(ray.put(A(1)))  # fail!

# Nothing happens when deregister an unavailable serializer.
ray.util.deregister_serializer(A)