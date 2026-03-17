import threading
import time

# Semaphores
# space: capacity for 50 pairs (100 particles)
# items: number of pairs ready for consumer
# mutex: ensures consecutive storage of pairs
space = threading.Semaphore(50) 
items = threading.Semaphore(0)
mutex = threading.Semaphore(1)

buffer = []

def producer(id):
    while True:
        # Produce pair
        p1, p2 = f"P{id}_a", f"P{id}_b"
        
        space.acquire()
        mutex.acquire()
        buffer.append(p1)
        buffer.append(p2)
        print(f"Producer {id} added {p1}, {p2}. Buffer size: {len(buffer)}")
        mutex.release()
        items.release()
        time.sleep(1)

def consumer():
    while True:
        items.acquire()
        # No mutex needed for consumer as there is only one consumer
        p1 = buffer.pop(0)
        p2 = buffer.pop(0)
        print(f"Consumer packaged {p1}, {p2}. Buffer size: {len(buffer)}")
        space.release()
        time.sleep(1.5)

# Start threads
threading.Thread(target=consumer, daemon=True).start()
for i in range(3):
    threading.Thread(target=producer, args=(i,), daemon=True).start()

time.sleep(10)