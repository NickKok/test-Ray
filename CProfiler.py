import cProfile  # Added import statement
import ray

def ex1():
    list1 = []
    for i in range(5):
        list1.append(ray.get(func.remote()))

def main():
    ray.init()
    cProfile.run('ex1()')  # Modified call to ex1
    cProfile.run('ex2()')
    cProfile.run('ex3()')

if __name__ == "__main__":
    main()