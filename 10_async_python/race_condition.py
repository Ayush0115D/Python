import threading
chai_stock = 0

def restock():
    global chai_stock
    for _ in range(10000):
        chai_stock += 1
# Create multiple threads to simulate race condition 
threads = [threading.Thread(target=restock) for _ in range(2)]
# Start all threads
for t in threads:
    t.start()
# Wait for all threads to complete
for t in threads:
    t.join()

print("Chai stock:", chai_stock)
