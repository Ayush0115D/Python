import threading
import time

def take_orders():
    for i in range(1,4):
        print(f"Taking order #{i}")
        time.sleep(1)  # Simulate time taken to take an order

def brew_chai():
    for i in range(1,4):
        print(f"Brewing chai #{i}")
        time.sleep(2)  # Simulate time taken to brew chai       
    #create threads
order_thread = threading.Thread(target=take_orders)
chai_thread = threading.Thread(target=brew_chai)
order_thread.start()
chai_thread.start() # Start the chai brewing thread
#wait for both to finish
order_thread.join()
chai_thread.join()
print("All orders taken and chai brewed!")    