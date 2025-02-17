import time


def time_it(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f"{func.__name__} took {int(end - start) * 1000}ms")
        return result
    return wrapper


@time_it
def some_op():
    print("Starting op")
    time.sleep(1)
    print("We are done")
    return


if __name__ == '__main__':
    # ti = time_it(some_op)
    # print(ti)
    # ti()
    some_op()