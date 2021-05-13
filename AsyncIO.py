import ray
import asyncio
ray.init()

@ray.remote
class AsyncActor:
    # multiple invocation of this method can be running in
    # the event loop at the same time
    async def run_concurrent(self):
        print("started")
        await asyncio.sleep(2) # concurrent workload here
        print("finished")

#actor = AsyncActor.remote()

# regular ray.get
#ray.get([actor.run_concurrent.remote() for _ in range(50)])

# async ray.get
#await actor.run_concurrent.remote()


#actor = AsyncActor.options(max_concurrency=10).remote()

# Only 10 tasks will be running concurrently. Once 10 finish, the next 10 should run.
#ray.get([actor.run_concurrent.remote() for _ in range(50)])


@ray.remote
class ThreadedActor:
    def task_1(self): print("I'm running in a thread!")
    def task_2(self): print("I'm running in another thread!")

a = ThreadedActor.options(max_concurrency=2).remote()
ray.get([a.task_1.remote(), a.task_2.remote()])