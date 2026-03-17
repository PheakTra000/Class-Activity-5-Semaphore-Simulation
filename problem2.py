import threading

# Initial values: a=1 (starts Process 1), others 0
a = threading.Semaphore(1)
b = threading.Semaphore(0)
c = threading.Semaphore(0)

def process_1():
    a.acquire()
    print("H", end="", flush=True)
    print("E", end="", flush=True)
    b.release()

def process_2():
    b.acquire()
    print("L", end="", flush=True)
    print("L", end="", flush=True)
    c.release()

def process_3():
    c.acquire()
    print("O", end="", flush=True)
    print()

threading.Thread(target=process_1).start()
threading.Thread(target=process_2).start()
threading.Thread(target=process_3).start()