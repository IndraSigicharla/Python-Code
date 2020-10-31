from threading import Thread, Lock
import time

database_value = 0


def increase(lock):
    global database_value
    # Context manager (without it, use lock.aquire() and lock.release())
    with lock:
        local_copy = database_value
        local_copy += 1
        time.sleep(0.1)
        database_value = local_copy


if __name__ == "__main__":

    lock = Lock()
    print("Start value", database_value)

    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("End value", database_value)

    print("End Main")
