import ray
import time

ray.init()

# Specify required resources for an actor.
@ray.remote
class Counter(object):
    def __init__(self):
        self.value = 0
    def increase(self):
        self.value += 1
        return self.value


# Create an actor from this class.
counter = Counter.remote()

obj_ref = counter.increase.remote()

print(ray.get(obj_ref))

"""
Methods called on different actors can execute in parallel, 
and methods called on the same actor are executed serially in the order that they are called. 
Methods on the same actor will share state with one another, as shown below.
"""

# Create ten Counter actors.
counters = [Counter.remote() for _ in range(4)]


# Increment each Counter once and get the results. These tasks all happen in
# parallel.
results = ray.get([c.increase.remote() for c in counters])
print(results) # prints [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


results = ray.get([counters[0].increase.remote() for _ in range(5) ])
print(results)


assert ray.is_initialized() == True

ray.shutdown()
assert ray.is_initialized() == False


