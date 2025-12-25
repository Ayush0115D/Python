import threading

counter = 0
lock = threading.Lock()

def increament():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

threads = [threading.Thread(target=increament) for _ in range(10)] # Create 10 threads
[t.start() for t in threads]# Start all threads
[t.join() for t in threads]# Wait for all to finish

print(f"Final counter: {counter}")
#🔍 Why lock is needed?
#counter += 1 is NOT atomic , meaning it consists of multiple steps.
# Internally:
# 1. Read counter
# 2. Add 1
# 3. Write back
# Without a lock, two threads could read the same value and overwrite each other ❌


#  What if we REMOVE the lock?
# counter += 1   # without lock
# Possible result:
# Final counter: 743921   ❌ (random, incorrect)
# Because:
# Multiple threads read the same value
# Updates get lost