from ray.util import ActorPool

a1, a2 = Actor.remote(), Actor.remote()
pool = ActorPool([a1, a2])
print(pool.map(lambda a,v: a.double.remote(v), [1,2,3,4]))