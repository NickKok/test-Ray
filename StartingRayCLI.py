import ray
#ray.init(address='auto')
ray.init()


@ray.remote(num_gpus=1)
class Foo(object):

    # Any method of the actor can return multiple object refs.
    @ray.method(num_returns=2)
    def bar(self):
        return 1, 2

f = Foo.remote()

obj_ref1, obj_ref2 = f.bar.remote()
assert ray.get(obj_ref1) == 1
assert ray.get(obj_ref2) == 2


@ray.remote(num_cpus=2, num_gpus=1)
class GPUActor(object):
    print(ray.get_gpu_ids())
    pass


test_obj = GPUActor.remote()




